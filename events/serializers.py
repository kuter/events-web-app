from rest_framework import serializers

from .models import Event
from .validators import is_valid_event_date


class EventSerializer(serializers.ModelSerializer):
    """Evernt object serializer."""

    class Meta:
        model = Event
        fields = ['title', 'description', 'date']

    def validate_date(self, value):
        return is_valid_event_date(value)
