from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Group
from .forms import GroupForm

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user
            group.save()
            group.members.add(request.user)
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()
    return render(request, 'groups/create_group.html', {'form': form})

@login_required
def search_groups(request):
    query = request.GET.get('query')
    interest = request.GET.get('interest')
    meeting_time = request.GET.get('meeting_time')

    groups = Group.objects.all()
    if query:
        groups = groups.filter(name__icontains=query)
    if interest:
        groups = groups.filter(interests__icontains=interest)
    if meeting_time:
        groups = groups.filter(meeting_time__icontains=meeting_time)

        
    return render(request, 'groups/search_groups.html', {'groups': groups})