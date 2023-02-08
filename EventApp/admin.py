from django.contrib import admin

from .models import Event, EventType


class EventAdmin(admin.ModelAdmin):
    fields = ('id', 'user', 'event_type', 'info', 'timestamp', 'created_at')
    readonly_fields = ('id', 'user', 'created_at',)
    list_filter = ('event_type', 'timestamp')


class EventTypeAdmin(admin.ModelAdmin):
    fields = ('id', 'name',)
    readonly_fields = ('id',)


admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
