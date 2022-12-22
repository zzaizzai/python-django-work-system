from django.db import models
from works.models import Work
# Create your models here.


class Commission(models.Model):
    title = models.CharField('commission title', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_due = models.DateField('Work due')
    team = models.IntegerField('department in charger', default=1)
    datetime_completed = models.DateTimeField(
        'completed datetime', blank=True, null=True)
    user_completed = models.IntegerField(
        'completed user', blank=True, null=True)
    work_id = models.ForeignKey(Work, blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.title