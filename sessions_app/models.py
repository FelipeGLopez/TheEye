from django.db import models

from events.models import Event


class Session(models.Model):
    """
    Every session has its id and its relation with the event.
    """

    session_id = models.CharField(max_length=100, unique=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
