from django import forms
from django.db import models
from .models import UserEntry

class UserEntryForm(forms.ModelForm):
    class Meta:
        model = UserEntry
        fields = ('header', 'description', 'link', 'email', 'image', 'uuid')

    
