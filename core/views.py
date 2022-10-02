from django.shortcuts import render
from .models import Companies, Documents
from .forms import CompaniesForms


def new_subscription(request):
    form = CompaniesForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form = CompaniesForms()

    return render(request, "core/new_subscription.html", {'form': form})












