from django.forms import ModelForm, Textarea, FileInput, DateTimeField, TextInput, DateInput, NumberInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Session

class Session_booking(forms.ModelForm):
    class Meta:
        model   =   Session
        fields  =   [
            'full_name',
            'mobile_number',
            'email_address',
            'facebook_link',
            'instagram_link',
            'youtube_link',
            'booking_date'
            
          
        ]
        widgets = {
            'booking_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
                      }),
            'mobile_number': NumberInput(attrs={'placeholder':'0701234567'}),
            'e_mail_address': TextInput(attrs={'placeholder':'johndoe@email.com'}),
            }