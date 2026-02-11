from django import forms
from events.models import Category,Event,Participant
from django.core.exceptions import ValidationError
from datetime import date

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400'})
        }

class EventForm(forms.ModelForm):
    # multiple participants field
    participant_to = forms.ModelMultipleChoiceField(
        queryset=Participant.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': 'w-full px-4 py-2 border rounded-lg'}
        )
    )
    
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400'}),
            'date': forms.DateInput(attrs={'type': 'date','class': 'w-full px-4 py-2 border rounded-lg'}),
            "participant_to": forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
        }

    def clean_date(self):
        event_date = self.cleaned_data.get["date"]
        if event_date < date.today():
            raise ValidationError("Event date cannot be in the past.")
        return event_date
    
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-400'})
        }
