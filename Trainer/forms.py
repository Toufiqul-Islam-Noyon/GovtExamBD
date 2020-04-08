from django import forms

from Trainer.models import Topic, ShortQuestion


class TopicFrom(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['TrainingName','TopicName']


class ShortQuestionFrom(forms.ModelForm):
    class Meta:
        model = ShortQuestion
        fields = ['TopicName','ShortQuestionName']