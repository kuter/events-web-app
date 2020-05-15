from django.contrib import admin

from .models import Event, EventParticipant


class EventParticipantInline(admin.TabularInline):  # noqa: D101
    model = EventParticipant
    extra = 0


class EventAdmin(admin.ModelAdmin):
    """Admin view for Event objects."""

    inlines = [
        EventParticipantInline,
    ]


admin.site.register(Event, EventAdmin)
