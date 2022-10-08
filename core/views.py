from django.shortcuts import render
from .forms import CompaniesForms
from django.contrib.auth.decorators import login_required


@login_required
def new_subscription(request):
    form = CompaniesForms(request.user, request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = CompaniesForms()

    return render(request, "core/new_subscription.html", {'form': form})












