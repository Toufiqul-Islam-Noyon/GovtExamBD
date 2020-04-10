"""GovtExamBD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views

from GovernmentEmployee.views import viewTrainingList
from users import views as user_views
from TrainerTakenCourse import views as trainer_views
from StudentTakenCourse import views as student_views
from django.conf.urls.static import static

from django.conf.urls.static import static
from GovernmentEmployee import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='courses'),
    path('GovernmentEmployeeHome/', views.GovernmentEmployeeHome, name='GovernmentEmployeeHome'),
    path('GovernmentEmployeeProfile/', views.GovernmentEmployeeProfile, name='GovernmentEmployeeProfile'),

    path('addTraining/', views.addTraining, name='addTraining'),
    path('viewTraining/', viewTrainingList.as_view(), name='viewTraining'),
    path('deleteTraining/<int:pk>', views.deleteTraining, name='deleteTraining'),
    path('editTraining/<int:pk>', views.updateTraining, name='editTraining'),
    path('detailsTraining/<int:pk>', views.detailsTraining, name='detailsTraining'),

    path('detailsCourse/<int:pk>', views.TrainingAndTopicListView, name='TrainingAndTopicListView'),


    path('addStudentTakenCourse/', student_views.StudentTakenCourse, name='addStudentTakenCourse'),
    path('viewStudentTakenCourse/', student_views.StudentTakenCourseList.as_view(), name='StudentTakenCourseView'),


    path('addTrainerTakenCourse/', trainer_views.addTrainerTakenCourse, name='addTrainerTakenCourse'),
    path('viewTrainerTakenCourse/', trainer_views.TrainerTakenCourseList.as_view(), name='ViewTrainerTakenCourse'),


    path('registerTrainer/',user_views.TrainerSignUpView.as_view(), name='registerTrainer'),
    path('viewRegisterTrainer/',user_views.RegTrainerList.as_view(), name='viewRegisterTrainer'),
    path('detailsRegisterTrainer/<int:pk>', user_views.detailsRegisterTrainer, name='detailsRegisterTrainer'),

    path('registerStudent/',user_views.StudentSignUpView.as_view(), name='registerStudent'),
    path('StudentRegisterView/', user_views.RegStudentList.as_view(), name='StudentRegisterView'),
    path('detailsRegisterStudent/<int:pk>', user_views.detailsRegisterStudent, name='detailsRegisterStudent'),

    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='GovernmentEmployee/PasswordChangeForm.html'), name='govt_password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),





]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

