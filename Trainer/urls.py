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

from McqQuestion.views import McqQuestionView
from Trainer import views
from Trainer.views import viewTopicListView, viewShortQuestion
from McqQuestion import views as Mcq_views

urlpatterns = [
    path('TrainerHome/', views.TrainerHome, name='TrainerHome'),
    path('TrainerProfile/', views.TrainerProfile, name='TrainerProfile'),
    path('addTopic/', views.addTopic, name='addTopic'),
    path('viewTopic/', viewTopicListView.as_view(), name='viewTopic'),
    path('deleteTopic/<int:pk>', views.deleteTopic, name='deleteTopic'),
    path('editTopic/<int:pk>', views.updateTopic, name='editTopic'),

    path('addMcqQuestion/', Mcq_views.addMcqQuestion, name='addMcqQuestion'),
    path('viewMcqQuestion/', McqQuestionView.as_view(), name='viewMcqQuestion'),
    path('deleteMcqQuestion/<int:pk>', Mcq_views.deleteMcqQuestion, name='deleteMcqQuestion'),
    path('editMcqQuestion/<int:pk>', Mcq_views.updateMcqQuestion, name='editMcqQuestion'),

    path('addShortQuestion/', views.addShortQuestion, name='addShortQuestion'),
    path('viewShortQuestion/', viewShortQuestion.as_view(), name='viewShortQuestion'),
    path('deleteShortQuestion/<int:pk>', views.deleteShortQuestion, name='deleteShortQuestion'),
    path('editShortQuestion/<int:pk>', views.updateShortQuestion, name='editShortQuestion'),

    # path('viewTrainingAsTopic/$', views.viewTrainingAsTopic, name='viewTrainingAsTopic'),


    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='Trainer/PasswordChangeForm.html'), name='trainer_password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]
