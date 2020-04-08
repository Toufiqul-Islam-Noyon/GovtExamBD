from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from GovernmentEmployee.models import Training


class Topic(models.Model):
    TrainingName = models.ForeignKey(Training,on_delete=models.CASCADE)
    TopicName = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.TopicName

    class Meta:
        db_table = "topic"

    def get_absolute_url(self):
        return reverse('Trainer:editTopic', kwargs={'pk': self.pk})


def create_slug(instance,new_slug = None):
    slug = slugify(instance.TopicName)
    if new_slug is not None:
        slug = new_slug
    qs = Topic.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver,sender=Topic)


# class Quiz(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quizzes')
#     name = models.CharField(max_length=255)
#     subject = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quizzes')
#
#     def __str__(self):
#         return self.name


class ShortQuestion(models.Model):
    TopicName = models.ForeignKey(Topic, on_delete=models.CASCADE)
    ShortQuestionName = models.TextField(max_length=250, default="")

    def __str__(self):
        return self.ShortQuestionName

    class Meta:
        db_table = "ShortQuestion"

