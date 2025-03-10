from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(User, related_name='meetup_groups')
    meeting_time = models.CharField(max_length=100, help_text='General meeting time, e.g., "Saturdays at 2pm"')
    interests = models.TextField(help_text='Comma-separated list of interests')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
