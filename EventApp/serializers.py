from rest_framework import serializers

from .models import Event, EventType


class EventCreateSerializer(serializers.ModelSerializer):
    event_type = serializers.CharField()
    info = serializers.JSONField()
    timestamp = serializers.DateTimeField()

    def create(self, validated_data):
        user = self.context['request'].user.id
        event_type = EventType.objects.filter(name=validated_data['event_type'])
        if not event_type.exists():
            event_type = EventType.objects.create(name=validated_data['event_type'])
            event_type.save()
        event_type = EventType.objects.get(name=validated_data['event_type'])
        event = Event.objects.create(event_type_id=event_type.id,
                                     info=validated_data['info'],
                                     timestamp=validated_data['timestamp'],
                                     user_id=user
                                     )
        event.save()
        return event

    class Meta:
        model = Event
        fields = ('event_type', 'info', 'timestamp')
