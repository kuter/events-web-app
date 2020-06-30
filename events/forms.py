import datetime

from django import forms

from .models import Event
from .validators import is_valid_event_date


class EventCreateForm(forms.ModelForm):
    """Event creation form."""

    class Meta:
        model = Event
        fields = ['title', 'description', 'date']

    def clean_date(self):
        """Check if future date.

        Returns:
            datetime: cleaned date

        Raises:
            ValidationError: when date is in the past
        """
        date = self.cleaned_data['date']
        return is_valid_event_date(date)
