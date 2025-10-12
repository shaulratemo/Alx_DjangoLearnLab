from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering new users.
    Automatically creates a token for the user after registration.
    """
    password = serializers.CharField(write_only=True)

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


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying or updating user profile information.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['followers']
