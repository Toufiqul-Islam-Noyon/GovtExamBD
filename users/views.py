from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from .decorators import teacher_required, parent_required
# from .forms import UserRegisterForm
from django.views.generic import CreateView, TemplateView, ListView
from GovernmentEmployee.models import Training
from McqQuestion.models import McqQuestion
from users.decorators import superAdmin_required, governmentEmployee_required, trainer_required, student_required
from .forms import GovernmentEmployeeSignUpForm, TrainerSignUpForm, StudentSignUpForm, SuperAdminSignUpForm, UserUpdateForm
from .models import User


class QuizTakenMcq(ListView):
    model = McqQuestion
    template_name = 'quizTakenMcq.html'
    context_object_name = 'object_list'
    paginate_by = 15


# Main User Interface
def BaseHome(request):
    training = Training.objects.all()
    user = User.objects.all()

    context = {
        'shelf': training,
        'Teacher_list': user
    }
    return render(request,'index.html',context)

    # model = Training
    # template_name = 'index.html'
    # context_object_name = 'shelf'
    # ordering = ['-date_posted']
    # paginate_by = 15


# after login to user
def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            messages.success(request,"Login Successfully")
            return redirect('SuperAdminhome')
        elif request.user.is_governmentEmployee:
            messages.success(request, "Login Successfully")
            return redirect('GovernmentEmployeeHome')
        elif request.user.is_trainer:
            messages.success(request, "Login Successfully")
            return redirect('TrainerHome')
        elif request.user.is_student:
            messages.success(request, "Login Successfully")
            return redirect('StudentProfile')
    return HttpResponse("login failed")


# SuperAdmin create code
@method_decorator([login_required, superAdmin_required], name='dispatch')
class SuperAdminSignUpView(CreateView):
    model = User
    form_class = SuperAdminSignUpForm
    template_name = 'SuperAdmin/SuperAdminRegister.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'superuser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)
        return redirect('viewRegisterSuperAdmin')


# def GovernmentEmployeeSignUpView(request):
#     if request.method == 'POST':
#         u_form = GovernmentEmployeeSignUpForm(request.POST)
#         p_form = GovernmentEmployeeFrom(request.POST)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated')
#             return redirect('viewRegisterGovt')
#
#     else:
#         u_form = GovernmentEmployeeSignUpForm()
#         p_form = GovernmentEmployeeFrom()
#
#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'SuperAdmin/GovernmentEmployeeRegister.html', context)


# Government Employee create code
@method_decorator([login_required, superAdmin_required], name='dispatch')
class GovernmentEmployeeSignUpView(SuccessMessageMixin,CreateView):
    model = User
    form_class = GovernmentEmployeeSignUpForm
    template_name = 'SuperAdmin/GovernmentEmployeeRegister.html'
    # success_message = "Government Employee %(username)s created successfully"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'governmentEmployee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)

        return redirect('viewRegisterGovt')


# Trainer create
@method_decorator([login_required, governmentEmployee_required], name='dispatch')
class TrainerSignUpView(CreateView):
    model = User
    form_class = TrainerSignUpForm
    template_name = 'GovernmentEmployee/TrainerRegisterForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'trainer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)
        return redirect('viewRegisterTrainer')


# Student create
@method_decorator([login_required, governmentEmployee_required], name='dispatch')
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'GovernmentEmployee/StudentRegisterForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        # login(self.request, user)
        messages.add_message(self.request, messages.INFO, 'Government Employee Created Successfully.')
        return redirect('StudentRegisterView')


# SuperAdmin Registration VIew
@method_decorator([login_required, superAdmin_required], name='dispatch')
class RegSuperAdminList(ListView):
    model = User
    template_name = 'SuperAdmin/SuperAdminRegisterView.html'
    paginate_by = 15


# SuperAdmin Registration Details
def detailsRegisterSuperAdmin(request,pk,template_name='SuperAdmin/SuperAdminRegisterDetails.html'):
    details = get_object_or_404(User, pk=pk)
    return render(request, template_name, {'object': details})


# SuperAdmin Registration Delete
def deleteRegisterSuperAdmin(request, pk, template_name='SuperAdmin/SuperAdminRegisterDelete.html'):
    user_delete = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_delete.delete()
        messages.success(request, f'Your SuperAdmin has been Deleted Successfully')
        return redirect('viewRegisterSuperAdmin')
    return render(request, template_name, {'object': user_delete})


# Government Employee Registration View
@method_decorator([login_required, superAdmin_required], name='dispatch')
class RegGovtEmployeeList(ListView):
    model = User
    template_name = 'SuperAdmin/GovernmentEmployeeRegisterView.html'
    paginate_by = 15


# Government Employee Registration View Details
def DetailsGovernmentEmployee(request,pk,template_name='SuperAdmin/GovernmentEmployeeRegisterDetails.html'):
    details = get_object_or_404(User, pk=pk)
    return render(request, template_name, {'object': details})


def deleteGovernmentEmployee(request, pk, template_name='SuperAdmin/GovernmentEmployeeRegisterDelete.html'):
    user_delete = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user_delete.delete()
        messages.success(request, f'Your Government Employee has been Deleted Successfully')
        return redirect('viewRegisterGovt')
    return render(request, template_name, {'object': user_delete})


# Trainer Registration View
@method_decorator([login_required, governmentEmployee_required], name='dispatch')
class RegTrainerList(ListView):
    model = User
    template_name = 'GovernmentEmployee/TrainerRegisterView.html'
    paginate_by = 15


# Student Registration View Details
def detailsRegisterTrainer(request, pk,template_name='GovernmentEmployee/TrainerRegisterDetails.html'):
    details = get_object_or_404(User, pk=pk)
    return render(request, template_name, {'object': details})


# Student Registration View
@method_decorator([login_required, governmentEmployee_required], name='dispatch')
class RegStudentList(ListView):
    model = User
    template_name = 'GovernmentEmployee/StudentRegisterView.html'
    paginate_by = 15


# Student Registration View Details
def detailsRegisterStudent(request, pk,template_name='GovernmentEmployee/StudentRegisterDetails.html'):
    details = get_object_or_404(User, pk=pk)
    return render(request, template_name, {'object': details})

