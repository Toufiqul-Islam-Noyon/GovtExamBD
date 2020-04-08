from django.contrib import admin

# Register your models here.
from Trainer.models import Topic, ShortQuestion

admin.site.register(Topic)
admin.site.register(ShortQuestion)
