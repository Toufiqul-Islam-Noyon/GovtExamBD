from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from GovernmentEmployee import forms
from GovernmentEmployee.forms import TrainingForm
from GovernmentEmployee.models import Training
from Trainer.models import Topic
from users.decorators import governmentEmployee_required
from users.forms import UserUpdateForm
from TrainerTakenCourse.models import TrainerTakenCourse


def GovernmentEmployeeProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('GovernmentEmployeeProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'GovernmentEmployee/GovernmentEmployeeProfile.html', context)


# training and topic view join for Main Navbar
def CourseDetails(request,pk):
    # course = Training.objects.filter(Topic__TrainingName=)
    course1 = Training.objects.filter(pk=pk)
    course2 = Topic.objects.filter(TrainingName=pk)
    course3 = TrainerTakenCourse.objects.filter(CourseName=pk)
    context = {
        'Course': course1,
        'Course1': course2,
        'Course2': course3
    }
    return render(request,'CourseDetails.html', context)


# training and topic view join for Government Employee Dashboard

def TrainingAndTopicListView(request,pk):
    # course = Training.objects.filter(Topic__TrainingName=)
    course1 = Training.objects.filter(pk=pk)
    course2 = Topic.objects.filter(TrainingName=pk)
    course3 = TrainerTakenCourse.objects.filter(CourseName=pk)

    context = {
        'Course': course1,
        'Course1': course2,
        'Course2': course3
    }
    return render(request,'GovernmentEmployee/TrainingAndTopicListView.html', context)


# home page show course view
# @method_decorator([login_required, governmentEmployee_required], name='dispatch')
class CourseList(ListView):
    model = Training
    template_name = 'course.html'
    context_object_name = 'shelf'
    ordering = ['-date_posted']
    paginate_by = 15


def GovernmentEmployeeHome(request):
    shelf = Training.objects.all()
    return render(request, 'GovernmentEmployee/GovernmentEmployeeNavbar.html', {'shelf': shelf})


def addTraining(request):
    if request.method == 'POST':
        form = TrainingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.username = request.user
            form.save()
            messages.success(request, "Training Created Successfully")
            return redirect('viewTraining')
        else:
            messages.error(request, "Training Not Created Successfully")
    else:
        form = TrainingForm()
    return render(request, 'GovernmentEmployee/TrainingFrom.html', {'form': form})


# @method_decorator([login_required, governmentEmployee_required], name='dispatch')
class viewTrainingList(ListView):
    model = Training
    template_name = 'GovernmentEmployee/TrainingView.html'
    context_object_name = 'object_list'
    ordering = ['-date_posted']
    paginate_by = 5


def deleteTraining(request, pk, template_name='GovernmentEmployee/Training_Confirm_Delete.html'):
    training = get_object_or_404(Training, pk=pk)
    if request.method == 'POST':
        training.delete()
        messages.success(request, "Training Deleted Successfully")
        return redirect('viewTraining')
    # else:
    #     messages.error(request, "Training Not Deleted Successfully")
    return render(request, template_name, {'object': training})


def updateTraining(request,pk):
    training = get_object_or_404(Training, pk=pk)
    form = TrainingForm(request.POST or None, request.FILES or None, instance=training)
    if form.is_valid():
        form.save()
        messages.success(request, "Training Updated Successfully")
        return redirect("viewTraining")
    # else:
    #     messages.error(request, "Training Not Updated Successfully")
    return render(request, 'GovernmentEmployee/TrainingFrom.html', {'form': form})


def detailsTraining(request,pk,template_name='GovernmentEmployee/TrainingDetails.html'):
    details = get_object_or_404(Training, pk=pk)
    return render(request, template_name, {'object': details})

