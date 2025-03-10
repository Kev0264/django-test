from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def register(request):
    return render(request, 'users/register.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def login(request):
    return render(request, 'users/login.html')

@login_required
def logout(request):
    return render(request, 'users/logout.html')

def change_password(request):
    return render(request, 'users/change_password.html')

def edit_profile(request):
    return render(request, 'users/edit_profile.html')
