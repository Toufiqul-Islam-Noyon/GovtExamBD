from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from SuperAdmin.models import Ministry


class MinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = ['MinistryName',
                  'MinisterName',
                  'Email']


