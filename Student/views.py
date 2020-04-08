from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from users.decorators import student_required
from users.forms import UserUpdateForm
from users.models import User


class TeacherListView(ListView):
    model = User
    template_name = 'TeacherView.html'
    context_object_name = 'Teacher_list'
    ordering = 'username'


@login_required
@student_required
def StudentProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('StudentProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Student/StudentProfileFrom.html', context)