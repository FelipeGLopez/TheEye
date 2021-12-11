from celery.utils.log import get_task_logger

from backend.celery import app
from events.models import Event
from sessions_app.models import Session

logger = get_task_logger(__name__)


@app.task(name="send_event")
def send_event(validated_data):
    session_id = validated_data["session_id"]
    category = validated_data["category"]
    name = validated_data["name"]
    data = validated_data["data"]
    timestamp = validated_data["timestamp"]

    event, _ = Event.objects.get_or_create(
        category=category,
        name=name,
        defaults={
            "category": category,
            "name": name,
            "data": data,
            "timestamp": timestamp,
        },
    )
    session, _ = Session.objects.get_or_create(
        session_id=session_id,
        defaults={"session_id": session_id, "event": event},
    )
