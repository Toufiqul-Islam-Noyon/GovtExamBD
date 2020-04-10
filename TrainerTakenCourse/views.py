from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from GovernmentEmployee.models import Training
from TrainerTakenCourse.forms import TrainerTakenCourseForm
from TrainerTakenCourse.models import TrainerTakenCourse


def addTrainerTakenCourse(request, template_name='TrainerTakenCourse/TrainerTakenCourseForm.html'):
    form = TrainerTakenCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Created Successfully")
        return redirect('ViewTrainerTakenCourse')
    return render(request, template_name, {'form': form})



class TrainerTakenCourseList(ListView):
    model = TrainerTakenCourse
    template_name = 'TrainerTakenCourse/TrainerTakenCourseView.html'
    paginate_by = 15