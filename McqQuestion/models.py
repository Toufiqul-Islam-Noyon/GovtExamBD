from django.db import models

# Create your models here.
from Trainer.models import Topic


class McqQuestion(models.Model):
    TopicName = models.ForeignKey(Topic,on_delete=models.CASCADE)
    McqQuestionName = models.TextField(max_length=250,default="")
    Choice1 = models.CharField(max_length=50, default="")
    Choice2 = models.CharField(max_length=50, default="")
    Choice3 = models.CharField(max_length=50, default="")
    Choice4 = models.CharField(max_length=50, default="")
    Choose = (('A', 'Choice1'), ('B', 'Choice2'), ('C', 'Choice3'), ('D', 'Choice4'))
    CorrectAnswer = models.CharField(max_length=1, choices=Choose)

    def __str__(self):
        return self.McqQuestionName

    class Meta:
        db_table = "mcqQuestion"