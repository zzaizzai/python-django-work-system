from . import views
from django.urls import path, include


urlpatterns = [
    path('all_commissions', views.all_commissions, name="all_commissions"),

]

