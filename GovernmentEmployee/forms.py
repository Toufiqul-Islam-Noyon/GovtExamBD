from django import forms
from django.contrib.auth.models import User
from GovernmentEmployee.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['TrainingCode','TrainingName', 'TrainingStartDate','TrainingDuration','picture']





