from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    name = models.CharField('team name', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, max_length=255)
    
    def __str__(self):
        return self.name


class Member_Team(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, blank=True, null=True, on_delete=models.SET_NULL)