from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from core.models import AppliedCompanies
from .forms import AppliedCompaniesForms



@login_required
def list_subscriptions(request):
    user = request.user
    data = AppliedCompanies.objects.filter(user=user).filter(active=True)
    context = {"data": data }
    return render(request, "core/list_subscriptions.html", context)


@login_required
def archived_subscriptions(request):
    user = request.user
    data = AppliedCompanies.objects.filter(user=user).filter(active=False)
    context = {"data": data }
    return render(request, "core/archived_subscription.html", context)   


@login_required
def new_subscription(request):
    form = AppliedCompaniesForms(request.user, request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = AppliedCompaniesForms()

    return render(request, "core/new_subscription.html", {'form': form})


@login_required
def edit_subscription(request, pk):
    data = get_object_or_404(AppliedCompanies, pk=pk)
    form = AppliedCompaniesForms(instance = data)
    if request.method == "POST": 
        form = AppliedCompaniesForms(request.user, request.POST, instance = data)
        if form.is_valid():
            form.save()
        return redirect('/list_subscriptions/')
    return render(request, "core/edit_subscription.html", {'form': form})


@login_required
def archive_or_active_subscription(request, pk):
    user = request.user
    data = get_object_or_404(AppliedCompanies, pk=pk)
    if data.user == user:
        if data.active == True:
            data.active = False
        else:
            data.active = True
    data.save()
    return redirect('/list_subscriptions/')


@login_required
def delete_subscription(request, pk):
    user = request.user
    data = get_object_or_404(AppliedCompanies, pk=pk)
    if data.user == user:
        data.delete()
    return redirect('/archived_subscriptions/')