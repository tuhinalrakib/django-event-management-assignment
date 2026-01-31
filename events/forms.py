from django import forms
from events.models import Category,Event,Participant
from django.core.exceptions import ValidationError
from datetime import date

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        field = "__all__"

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        field = "__all__"

    def clean_date(self):
        event_date = self.cleaned_data.get["date"]
        if event_date < date.today():
            raise ValidationError("Event date cannot be in the past.")
        return event_date
    
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"

