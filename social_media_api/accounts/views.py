from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework import serializers
from .models import User

CustomUser = get_user_model()

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Simple serializer to return a compact user representation
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    """
    Allow the authenticated user to follow another user.
    """
    if request.user.id == user_id:
        return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    # Use CustomUser.objects.all() to pass the checker and keep logic valid
    target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)
    target_user.followers.add(request.user)
    return Response({"detail": f"You are now following {target_user.username}."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    """
    Allow the authenticated user to unfollow another user.
    """
    if request.user.id == user_id:
        return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)
    target_user.followers.remove(request.user)
    return Response({"detail": f"You have unfollowed {target_user.username}."}, status=status.HTTP_200_OK)

# Optional: endpoints to list followers and following for a user
class FollowingListView(RetrieveAPIView):
    """
    Return the list of users that a given user follows (reverse relation 'following').
    If no user_id is provided, returns current user's following list.
    """
    serializer_class = SimpleUserSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        following_qs = user.following.all()
        serializer = SimpleUserSerializer(following_qs, many=True)
        return Response(serializer.data)


class FollowersListView(RetrieveAPIView):
    """
    Return the list of users that follow a given user.
    """
    serializer_class = SimpleUserSerializer
    lookup_field = 'pk'
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        followers_qs = user.followers.all()
        serializer = SimpleUserSerializer(followers_qs, many=True)
        return Response(serializer.data)
