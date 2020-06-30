import datetime

from django import forms

from .models import Event


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
        if date <= datetime.date.today():
            raise forms.ValidationError('You cannot create event in the past')
        return date
