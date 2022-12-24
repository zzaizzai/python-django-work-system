from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

# Create your models here.


class Work(models.Model):
    title = models.CharField('Work title', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)
    date_due = models.DateField('Work due')
    team = models.ForeignKey(
        Team, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(
        'Work description', max_length=255, null=True)
    datetime_completed = models.DateTimeField(
        'completed datetime', blank=True, null=True)
    user_completed = models.IntegerField(
        'completed user', blank=True, null=True)

    def __str__(self):
        return self.title
