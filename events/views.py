from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.serializers import EventSerializer


class CreateEventViewSet(mixins.CreateModelMixin):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
