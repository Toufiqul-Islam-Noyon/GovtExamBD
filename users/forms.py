from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
# from .models import Profile
from .models import User


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','phone_number','Address','image']


# super admin registration form
class SuperAdminSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        if commit:
            user.save()
        return user


# government employee registration form
class GovernmentEmployeeSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email','MinistryName', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_governmentEmployee = True
        if commit:
            user.save()
        return user


# trainer registration form
class TrainerSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_trainer = True
        if commit:
            user.save()
        return user


# student registration form
class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user


# password change form
class PasswordChangeFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['password1', 'password2']


