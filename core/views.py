from django.shortcuts import get_object_or_404, redirect, render

from core.models import Companies
from .forms import CompaniesForms
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db import transaction
from django.urls import reverse_lazy


@login_required
def list_subscriptions(request):
    user = request.user
    data = Companies.objects.filter(user=user)
    context = {"data": data }
    return render(request, "core/list_subscriptions.html", context)


@login_required
def new_subscription(request):
    form = CompaniesForms(request.user, request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = CompaniesForms()

    return render(request, "core/new_subscription.html", {'form': form})


@login_required
def edit_subscription(request, pk):
    data = Companies.objects.get(pk=pk)
    form = CompaniesForms(instance = data)
    if request.method == "POST": 
        form = CompaniesForms(request.user, request.POST, instance = data)
        if form.is_valid():
            form.save()
        return redirect('/list_subscriptions/')
    return render(request, "core/edit_subscription.html", {'form': form})


@login_required
def delete_subscription(request, pk):
    data = get_object_or_404(Companies, pk=pk)
    data.delete()
    return redirect('/list_subscriptions/')
