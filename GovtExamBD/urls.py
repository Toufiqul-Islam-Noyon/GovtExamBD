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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from GovernmentEmployee import views as Govt_views
from Student.views import TeacherListView
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SuperAdmin/',include('SuperAdmin.urls')),
    path('GovernmentEmployee/',include('GovernmentEmployee.urls')),
    path('Trainer/',include('Trainer.urls')),
    path('Student/',include('Student.urls')),
    path('Teacher/', TeacherListView.as_view(), name='TeacherListView'),
    # path('TeacherView/', TeacherListViewHomePage.as_view(), name='TeacherListView'),


    path('TrainingDetailsCourse/<int:pk>', Govt_views.CourseDetails, name='CourseDetails'),

    # users apps er views.py url
    # path('profile/', user_views.profile, name='profile'),
    path('home/', user_views.home, name='home'),
    path('BaseHome/', user_views.BaseHome, name='BaseHome'),
    path('', user_views.BaseHome, name='BaseHome'),
    path('quiz/',user_views.QuizTakenMcq.as_view(), name = 'QuizTakenMcq'),
    # path('registerSuperAdmin/', user_views.SuperAdminSignUpView.as_view(), name='registerSuperAdmin'),
    # path('viewRegisterSuperAdmin/', user_views.RegSuperAdminList.as_view(), name='viewRegisterSuperAdmin'),
    # path('registerTrainer/',user_views.TrainerSignUpView.as_view(), name='registerTrainer'),
    # path('registerGovt/',user_views.GovernmentEmployeeSignUpView.as_view(), name='registerGovt'),
    # path('viewRegisterGovt/',user_views.RegGovtEmployeeList.as_view(), name='viewRegisterGovt'),
    # path('viewRegisterTrainer/',user_views.RegTrainerList.as_view(), name='viewRegisterTrainer'),
    # path('SuperAdmin_password-change/',auth_views.PasswordChangeView.as_view(
    #                                            template_name='SuperAdmin/SuperAdminPasswordChangeForm.html'),name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
    #                                    template_name='users/password_change_done.html'), name='password_change_done'),

    # authentication er jonno default url
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
