from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework.utils import json

from GovernmentEmployee.models import Training
from StudentTakenCourse.forms import StudentTakenCourseForm
from StudentTakenCourse.models import StudentTakenCourse
from users.decorators import governmentEmployee_required
from django.shortcuts import render

from users.models import User


@login_required
@governmentEmployee_required
def StudentTakenCourse(request, template_name='StudentTakenCourse/StudentTakenCourseForm.html'):
    form = StudentTakenCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Created Successfully")
        return redirect('addStudentTakenCourse')
    return render(request, template_name, {'form': form})





class StudentTakenCourseList(ListView):
    model = StudentTakenCourse
    template_name = 'StudentTakenCourse/StudentTakenCourseView.html'
    paginate_by = 15







