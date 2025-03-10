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
            return redirect('groups:group_detail', group_id=group.id)
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

@login_required
def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, 'groups/group_detail.html', {'group': group})

@login_required
def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups:group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/edit_group.html', {'form': form, 'group': group})

@login_required
def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('core:home')

@login_required
def join_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.members.add(request.user)
    return redirect('groups:group_detail', group_id=group_id)