from rest_framework import serializers

from events.models import Event
from sessions_app.models import Session


class EventSerializer(serializers.ModelSerializer):
    session_id = serializers.CharField()
    category = serializers.FloatField()
    name = serializers.FloatField()
    data = serializers.JSONField()
    timestamp = serializers.DateTimeField()

    class Meta:
        model = Event

    def create(self, validated_data):
        session_id = validated_data.pop("session_id")
        event = Event.objects.create(**validated_data)
        Session.objects.create(session_id=session_id, event=event)
        return event
