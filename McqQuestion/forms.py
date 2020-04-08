from django import forms

from McqQuestion.models import McqQuestion


class McqQuestionForm(forms.ModelForm):

    class Meta:
        model = McqQuestion
        fields = ['TopicName', 'McqQuestionName', 'Choice1', 'Choice2','Choice3','Choice4','CorrectAnswer']