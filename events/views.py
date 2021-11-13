from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.serializers import EventSerializer


class CreateEventViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
