from django.urls import path
from . import views

urlpatterns = [
    path('all_works', views.all_works, name='all_works'),

]
