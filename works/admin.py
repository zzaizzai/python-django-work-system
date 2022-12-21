from django.contrib import admin
from .models import Work
# Register your models here.




@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','updated_at']
    ordering = ('-created_at',)