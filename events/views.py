import logging

from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event
from events.serializers import EventSerializer
from events.tasks import send_event

logger = logging.getLogger(__name__)


class CreateEventApiView(APIView):
    """
    Create event api view.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Responsible for processing the events.
        """

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            send_event.delay(validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
