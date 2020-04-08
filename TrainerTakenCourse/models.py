from django.db import models
from django.conf import settings
# Create your models here.
from django.urls import reverse

from GovernmentEmployee.models import Training


class TrainerTakenCourse(models.Model):
    TrainerName = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    limit_choices_to={'is_trainer': True}, )
    CourseName = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.TrainerName)

    def get_absolute_url(self):
        return reverse('editTrainerTakenCourse', kwargs={'pk': self.pk})

