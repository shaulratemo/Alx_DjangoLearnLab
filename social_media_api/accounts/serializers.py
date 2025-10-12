from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering new users.
    Automatically creates a token for the user after registration.
    """
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user instance using Django's user creation method
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # Optional: set bio and profile picture if provided
        user.bio = validated_data.get('bio', '')
        user.profile_picture = validated_data.get('profile_picture', None)
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)
        return user
    

class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    Expects 'username' and 'password' fields in input.
    On validation it authenticates the user and ensures an auth token exists.
    The serializer returns the authenticated user as validated_data (so views can
    create the response containing Token and user info).
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        # Ensure a token exists for the user (create if missing)
        Token.objects.get_or_create(user=user)

        # Return the user so the view can access it via serializer.validated_data
        return user
    

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying or updating user profile information.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']
