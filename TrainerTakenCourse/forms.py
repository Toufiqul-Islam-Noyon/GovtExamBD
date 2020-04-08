from django import forms

from TrainerTakenCourse.models import TrainerTakenCourse


# Trainer taken course form
class TrainerTakenCourseForm(forms.ModelForm):
    class Meta:
        model = TrainerTakenCourse
        fields = ['TrainerName','CourseName']