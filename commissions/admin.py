from django.contrib import admin
from .models import Commission
# Register your models here.


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'team', 'created_at']
    ordering = ('-created_at',)
