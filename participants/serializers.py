from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User object serializer."""

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate_password(self, value):
        """Check password against password validators."""
        validate_password(value)
        return value

    def create(self, validated_data):
        """Create User instance with given password."""
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

# flake8: noqa DAR201, DAR101
