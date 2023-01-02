from django.db import models
from works.models import Work
from django.contrib.auth.models import User
from teams.models import Team
from ckeditor.fields import RichTextField
import datetime
# Create your models here.


class Commission(models.Model):
    title = models.CharField('commission title', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True)
    date_due = models.DateField('Work due')
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE)
    datetime_completed = models.DateTimeField(
        'completed datetime', blank=True, null=True)
    user_completed = models.IntegerField(
        'completed user', blank=True, null=True)
    parent_work = models.ForeignKey(
        Work, blank=True, null=True, on_delete=models.SET_NULL)
    # description = models.CharField(
    # 'description', blank=True, null=True, max_length=10000)
    description = RichTextField(blank=True, null=True)
    is_cancled = models.BooleanField(default=False)
    priority_point = models.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        return self.title

    @property
    def priority(self) -> int:

        now = datetime.datetime.now().date()

        days_differ_due = self.date_due - now
        days_differ_created = self.created_at.date() - now

        days_due = days_differ_due.days
        days_created = days_differ_created.days

        point_sum = -days_due*self.priority_point*2 - days_created*self.priority_point

        # canled or completed one has low priority
        if self.is_cancled or self.datetime_completed:
            point_sum -= 100

        return point_sum


class CommissionComment(models.Model):
    parent_commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(
        'Work description', max_length=500, blank=True,  null=True)


class CommissionHistory(models.Model):
    parent_commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    kind = models.CharField('add, view, edit, cancle', max_length=100)

    def __str__(self):
        return self.created_by.username + ' ' + self.kind
