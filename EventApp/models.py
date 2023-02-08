import uuid
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='Id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    event_type = models.ForeignKey('EventType', on_delete=models.PROTECT, verbose_name='Event type')
    info = models.JSONField(verbose_name='Info JSON')
    timestamp = models.DateTimeField(verbose_name='Timestamp')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f"{self.id}-Event"

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"


class EventType(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='Id')
    name = models.CharField(max_length=256, db_index=True, verbose_name='Name')

    def __str__(self):
        return f"{self.id}-{self.name}"

    class Meta:
        verbose_name = "Event type"
        verbose_name_plural = "Event types"
