from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """Events API view."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
