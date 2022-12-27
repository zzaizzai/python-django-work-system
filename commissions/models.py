from django.db import models
from works.models import Work
from django.contrib.auth.models import User
from teams.models import Team
# Create your models here.


class Commission(models.Model):
    title = models.CharField('commission title', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)
    date_due = models.DateField('Work due')
    team = models.ForeignKey(
        Team, blank=True, null=True, on_delete=models.SET_NULL)
    datetime_completed = models.DateTimeField(
        'completed datetime', blank=True, null=True)
    user_completed = models.IntegerField(
        'completed user', blank=True, null=True)
    parent_work = models.ForeignKey(
        Work, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(
        'description', blank=True, null=True, max_length=10000)
    is_cancled = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CommissionComment(models.Model):
    parent_commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(
        'Work description', max_length=500, blank=True,  null=True)
