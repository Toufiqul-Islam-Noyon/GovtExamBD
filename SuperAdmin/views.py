
# from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator

from SuperAdmin.models import Ministry
from users.decorators import superAdmin_required
from users.forms import UserUpdateForm
from users.models import User
from .forms import MinistryForm
from django.db.models import Count,Sum


def SuperAdminProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('SuperAdminProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'SuperAdmin/SuperAdminProfileFrom.html', context)


def SuperAdminhome(request):
    return render(request,'SuperAdmin/SuperAdminNavbar.html')


def SuperAdminDashBoard(request):
    ministry = Ministry.objects.count()
    return render(request,'SuperAdmin/Dashboard.html',{'ministry':ministry})


def viewMinistry(request, template_name='SuperAdmin/MinistryView.html'):
    contact_list = Ministry.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, template_name, {'contacts': contacts})


def addMinistry(request, template_name='SuperAdmin/MinistryFrom.html'):
    form = MinistryForm(request.POST or None)
    if form.is_valid():
        form.instance.username = request.user
        form.save()
        messages.success(request, f'Your Ministry has been Created Successfully')
        return redirect('addMinistry')
    # else:
    #     messages.error(request, f'Your Ministry has been Not Created Successfully')
    return render(request, template_name, {'form':form})


def updateMinistry(request, pk, template_name='SuperAdmin/MinistryFrom.html'):
    ministry = get_object_or_404(Ministry, pk=pk)
    form = MinistryForm(request.POST or None, instance=ministry)
    if form.is_valid():
        form.save()
        messages.success(request, f'Your Ministry Account Successfully Update')
        return redirect('viewMinistry')
    # else:
    #     messages.warning(request, f'Your Ministry Account Not Successfully Update')
    return render(request, template_name, {'form': form})


def deleteMinistry(request, pk, template_name='SuperAdmin/Ministry_confirm_delete.html'):
    ministry = get_object_or_404(Ministry, pk=pk)
    if request.method == 'POST':
        ministry.delete()
        messages.success(request, f'Your Ministry has been Deleted Successfully')
        return redirect('viewMinistry')
    return render(request, template_name, {'object': ministry})


def detailsMinistry(request,pk,template_name='SuperAdmin/MinistryDetails.html'):
    details = get_object_or_404(Ministry, pk=pk)
    return render(request, template_name, {'object': details})


def Password_Change(request):
    return render(request, 'SuperAdmin/SuperAdminPasswordChangeForm.html')

