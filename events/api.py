from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """Events API view."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        """Add user to request.data."""
        request.data.update({'user': request.user.pk})
        return super().create(request, *args, **kwargs)
