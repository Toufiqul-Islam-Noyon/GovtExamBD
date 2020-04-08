from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.contrib import messages
from McqQuestion.forms import McqQuestionForm
from McqQuestion.models import McqQuestion
from users.decorators import trainer_required


@login_required
@trainer_required
def addMcqQuestion(request, template_name='McqQuestion/McqQuestionForm.html'):
    form = McqQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Created Successful !")
        return redirect('viewMcqQuestion')
    return render(request, template_name, {'form': form})


@method_decorator([login_required, trainer_required], name='dispatch')
class McqQuestionView(ListView):
    model = McqQuestion
    template_name = 'McqQuestion/McqQuestionView.html'
    context_object_name = 'object_list'
    paginate_by = 15


@login_required
@trainer_required
def updateMcqQuestion(request, pk, template_name='McqQuestion/McqQuestionForm.html'):
    form = get_object_or_404(McqQuestion, pk=pk)
    form = McqQuestionForm(request.POST or None, instance=form)
    if form.is_valid():
        form.save()
        messages.success(request, "Updated Successful !")
        return redirect('viewMcqQuestion')
    return render(request, template_name, {'form': form})


@login_required
@trainer_required
def deleteMcqQuestion(request, pk, template_name='McqQuestion/McqQuestion_confirm_delete.html'):
    form = get_object_or_404(McqQuestion, pk=pk)
    if request.method == 'POST':
        form.delete()
        messages.success(request, "Deleted Successful !")
        return redirect('viewMcqQuestion')
    return render(request, template_name, {'object': form})
