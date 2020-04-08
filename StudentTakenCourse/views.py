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
def addStudentTakenCourse(request, template_name='StudentTakenCourse/StudentTakenCourseForm.html'):
    training = Training.objects.all()
    form = StudentTakenCourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Created Successfully")
        return redirect('StudentTakenCourseView')
    return render(request, template_name, {'form': form,'object':training})


# @method_decorator([login_required, governmentEmployee_required], name='dispatch')
class StudentTakenCourseList(ListView):
    model = StudentTakenCourse
    template_name = 'StudentTakenCourse/StudentTakenCourseView.html'
    paginate_by = 15
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super(StudentTakenCourseList, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context






