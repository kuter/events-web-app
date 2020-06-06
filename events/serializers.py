from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """Evernt object serializer."""

    class Meta:
        model = Event
        fields = '__all__'
