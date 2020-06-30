from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """Events API view."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        """Add user to request.data."""
        serializer.save(user=self.request.user)

# flake8: noqa DAR201
