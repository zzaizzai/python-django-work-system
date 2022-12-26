from django.contrib import admin
from .models import Commission, CommissionComment
# Register your models here.


@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'team', 'created_at']
    ordering = ('-created_at',)


@admin.register(CommissionComment)
class CommissionCommentAdmin(admin.ModelAdmin):
    list_display = ['description', 'created_at']
    ordering = ('-created_at',)