from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.utils import timezone
from PIL import Image
from SuperAdmin.models import Ministry


class Training(models.Model):
    TrainingCode = models.IntegerField(help_text='please enter a number ')
    TrainingName = models.CharField(max_length=150)
    # slug = models.SlugField(max_length=150, unique=True)
    TrainingStartDate = models.DateField()
    TrainingDuration = models.CharField(max_length=15, help_text='6 months')
    picture = models.ImageField(default='default.jpg', upload_to='Training_Pic/')
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.TrainingName

    class Meta:
        db_table = "training"

    def get_absolute_url(self):
        return reverse('editTraining', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Training, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)


# def create_slug(instance,new_slug = None):
#     slug = slugify(instance.TrainingName)
#     if new_slug is not None:
#         slug= new_slug
#     qs = Training.objects.filter(slug=slug).order_by("-id")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" %(slug,qs.first().id)
#         return  create_slug(instance,new_slug=new_slug)
#     return slug
#
#
# def pre_save_post_receiver(sender,instance,*args,**kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
#
# pre_save.connect(pre_save_post_receiver,sender=Training)








