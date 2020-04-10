from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse

from GovernmentEmployee.models import Training


class StudentTakenCourse(models.Model):
    StudentName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    limit_choices_to={'is_student': True},)
    CourseName = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.StudentName)

    def get_absolute_url(self):
        return reverse('editStudentTakenCourse', kwargs={'pk': self.pk})