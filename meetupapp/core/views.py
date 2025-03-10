from django.shortcuts import render

from groups.models import Group

def home(request):
    featured_groups = Group.objects.all()[:5] # Get the first 5 groups
    return render(request, 'core/home.html', {'featured_groups': featured_groups})
