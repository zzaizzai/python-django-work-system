from django.contrib import admin
from .models import Team, Member_Team
# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=['name', 'created_at']
    ordering = ('-created_at',)

@admin.register(Member_Team)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['member', 'team']
