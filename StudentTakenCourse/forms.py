from django import forms
from StudentTakenCourse.models import StudentTakenCourse


class StudentTakenCourseForm(forms.ModelForm):
    class Meta:
        model = StudentTakenCourse
        fields = ['StudentName','CourseName']