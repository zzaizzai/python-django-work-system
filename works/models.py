from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Work(models.Model):
    title = models.CharField('Work title', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField( blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_due = models.DateField('Work due')
    department_charge = models.IntegerField('department in charger', default=1)
    description = models.CharField(
        'Work description', max_length=255, null=True)
    workers = models.ManyToManyField(User, blank=True)
    datetime_completed = models.DateTimeField('completed datetime', blank=True, null=True)
    user_completed = models.IntegerField(
        'completed user', blank=True, null=True)



    def __str__(self):
        return self.title