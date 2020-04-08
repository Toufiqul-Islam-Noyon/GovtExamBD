from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.contrib import messages
from GovernmentEmployee.models import Training
from Trainer.forms import TopicFrom, ShortQuestionFrom
from Trainer.models import Topic, ShortQuestion
from users.decorators import trainer_required
from users.forms import UserUpdateForm


# @login_required
# @trainer_required
def TrainerHome(request):
    return render(request,'Trainer/TrainerNavbar.html')


# @login_required
# @trainer_required
def TrainerProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('TrainerProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Trainer/TrainerProfileFrom.html', context)


# @method_decorator([login_required, trainer_required], name='dispatch')
class viewTrainingAsTopic(ListView):
    model = Training
    template_name = 'Trainer/TrainingView.html'
    context_object_name = 'object_list'
    paginate_by = 15
    # training = Training.objects.all()
    # paginator = Paginator(training, 5)  # Show 25 contacts per page
    # page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    # return render(request, template_name, {'object_list': contacts})


# @login_required
# @trainer_required
def addTopic(request):
    if request.method == 'POST':
        form = TopicFrom(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Created Successfully !")
            return redirect('addTopic')
    else:
        form = TopicFrom()
    return render(request, 'Trainer/TopicForm.html', {'form': form})


# @method_decorator([login_required, trainer_required], name='dispatch')
class viewTopicListView(ListView):
    model = Topic
    template_name = 'Trainer/TopicView.html'
    context_object_name = 'object_list'
    paginate_by = 15
    # topic = Topic.objects.all()
    # paginator = Paginator(topic, 4)  # Show 25 contacts per page
    # page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    # data = {'object_list': contacts}
    # return render(request, template_name, data)


# @login_required
# @trainer_required
def deleteTopic(request, pk, template_name='Trainer/Topic_Confirm_Delete.html'):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'POST':
        topic.delete()
        messages.success(request, "Deleted Successfully !")
        return redirect('viewTopic')
    return render(request, template_name, {'object': topic})


# @login_required
# @trainer_required
def updateTopic(request,pk):
    topic = get_object_or_404(Topic, pk=pk)
    form = TopicFrom(request.POST or None, instance=topic)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully !")
        return redirect("viewTopic")
    return render(request, 'Trainer/TopicForm.html', {'form': form})


# @login_required
# @trainer_required
def addShortQuestion(request):
    if request.method == 'POST':
        form = ShortQuestionFrom(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Created Successfully !")
            return redirect('viewShortQuestion')
    else:
        form = ShortQuestionFrom()
    return render(request, 'Trainer/ShortQuestionFrom.html', {'form': form})


# @method_decorator([login_required, trainer_required], name='dispatch')
class viewShortQuestion(ListView):
    model = ShortQuestion
    template_name = 'Trainer/ShortQuestionView.html'
    context_object_name = 'object_list'
    paginate_by = 15
    # topic = ShortQuestion.objects.all()
    # data = {'object_list': topic}
    # return render(request, template_name, data)


# @login_required
# @trainer_required
def deleteShortQuestion(request, pk, template_name='Trainer/ShortQuestion_Confirm_Delete.html'):
    topic = get_object_or_404(ShortQuestion, pk=pk)
    if request.method == 'POST':
        topic.delete()
        messages.success(request, "Deleted Successfully !")
        return redirect('viewShortQuestion')
    return render(request, template_name, {'object': topic})


# @login_required
# @trainer_required
def updateShortQuestion(request,pk):
    topic = get_object_or_404(ShortQuestion, pk=pk)
    form = ShortQuestionFrom(request.POST or None, instance=topic)
    if form.is_valid():
        form.save()
        messages.success(request, "Update Successfully !")
        return redirect("viewShortQuestion")
    return render(request, 'Trainer/ShortQuestionFrom.html', {'form': form})
