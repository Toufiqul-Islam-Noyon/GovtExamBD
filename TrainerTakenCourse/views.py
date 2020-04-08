from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from GovernmentEmployee.models import Training
from TrainerTakenCourse.forms import TrainerTakenCourseForm
from TrainerTakenCourse.models import TrainerTakenCourse


# Trainer Taken Course insert CODE
def addTrainerTakenCourse(request, template_name='TrainerTakenCourse/TrainerTakenCourseForm.html'):
    training = Training.objects.all()
    form = TrainerTakenCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Created Successfully")
        return redirect('ViewTrainerTakenCourse')
    return render(request, template_name, {'form': form,'object':training})


# Trainer Taken Course View code
class TrainerTakenCourseList(ListView):
    model = TrainerTakenCourse
    template_name = 'TrainerTakenCourse/TrainerTakenCourseView.html'
    paginate_by = 15