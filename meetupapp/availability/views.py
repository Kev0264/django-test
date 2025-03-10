from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GeneralAvailability, AvailabilityOverride
from .forms import GeneralAvailabilityForm, AvailabilityOverrideForm

@login_required
def update_availability(request):
    general_availability, created = GeneralAvailability.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = GeneralAvailabilityForm(request.POST, instance=general_availability)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = GeneralAvailabilityForm(instance=general_availability)
    return render(request, 'availability/update_availability.html', {'form': form})

@login_required
def add_override(request):
    if request.method == 'POST':
        form = AvailabilityOverrideForm(request.POST)
        if form.is_valid():
            override = form.save(commit=False)
            override.user = request.user
            override.save()
            return redirect('profile')
    else:
        form = AvailabilityOverrideForm()
    return render(request, 'availability/add_override.html', {'form': form})
