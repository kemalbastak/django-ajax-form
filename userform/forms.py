from django import forms
from django.db import models
from .models import UserEntry

class UserEntryForm(forms.ModelForm):
    class Meta:
        model = UserEntry
        fields = ('header', 'description', 'link', 'email', 'image')

    def __init__(self, *args, **kwargs):
        super(UserEntryForm, self).__init__(*args, **kwargs)
        self.fields['header'].widget.attrs["placeholder"] = "Başlık"
        self.fields['description'].widget.attrs["placeholder"] = "Açıklama"
        self.fields['link'].widget.attrs["placeholder"] = "Link"
        self.fields['email'].widget.attrs["placeholder"] = "E-Mail"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"