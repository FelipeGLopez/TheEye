from rest_framework import serializers


class EventSerializer(serializers.Serializer):
    session_id = serializers.CharField()
    category = serializers.CharField()
    name = serializers.CharField()
    data = serializers.JSONField()
    timestamp = serializers.DateTimeField()
