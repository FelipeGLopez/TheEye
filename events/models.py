from django.db import models


class Event(models.Model):
    """
    An event has a category, a name and the payload of data.
    Also, it contains a timestamp with the data and time it occurred.
    """

    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    data = models.JSONField()
    timestamp = models.DateTimeField()

    @property
    def type(self):
        """Get the type (category + name)"""
        return self.category + " " + self.name
