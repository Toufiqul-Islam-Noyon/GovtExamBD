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

from django.urls import path
from django.contrib.auth import views as auth_views
from SuperAdmin import views
from users import views as user_views


urlpatterns = [
    path('SuperAdminHome/',views.SuperAdminhome, name='SuperAdminhome'),
    path('SuperAdminDashBoard/',views.SuperAdminDashBoard, name='SuperAdminDashBoard'),
    path('SuperAdminProfile/',views.SuperAdminProfile, name='SuperAdminProfile'),
    path('addMinistry/', views.addMinistry, name='addMinistry'),
    path('viewMinistry/', views.viewMinistry, name='viewMinistry'),
    path('editMinistry/<int:pk>', views.updateMinistry, name='editMinistry'),
    path('deleteMinistry/<int:pk>', views.deleteMinistry, name='deleteMinistry'),
    path('detailsMinistry/<int:pk>', views.detailsMinistry, name='detailsMinistry'),

    path('Password_Change/<int:pk>', views.Password_Change, name='Password_Change'),

    path('registerSuperAdmin/', user_views.SuperAdminSignUpView.as_view(), name='registerSuperAdmin'),
    path('viewRegisterSuperAdmin/', user_views.RegSuperAdminList.as_view(), name='viewRegisterSuperAdmin'),
    path('detailsRegisterSuperAdmin/<int:pk>', user_views.detailsRegisterSuperAdmin, name='detailsRegisterSuperAdmin'),
    path('deleteRegisterSuperAdmin/<int:pk>', user_views.deleteRegisterSuperAdmin, name='deleteRegisterSuperAdmin'),

    path('DetailsGovernmentEmployee/<int:pk>', user_views.DetailsGovernmentEmployee, name='DetailsGovernmentEmployee'),

    path('registerGovt/', user_views.GovernmentEmployeeSignUpView.as_view(), name='registerGovt'),
    path('deleteGovernmentEmployee/<int:pk>', user_views.deleteGovernmentEmployee, name='deleteGovernmentEmployee'),
    # path('registerGovt/', user_views.GovernmentEmployeeSignUpView, name='registerGovt'),

    path('viewRegisterGovt/', user_views.RegGovtEmployeeList.as_view(), name='viewRegisterGovt'),

    path('SuperAdmin_password-change/',auth_views.PasswordChangeView.as_view(template_name='SuperAdmin/SuperAdminPasswordChangeForm.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    # path('viewRegisterGovt/', views.viewRegisterGovt, name='viewRegisterGovt'),



]
