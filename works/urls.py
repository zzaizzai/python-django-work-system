from django.urls import path
from . import views

urlpatterns = [
    path('all_works', views.all_works, name='all_works'),
    path('add_work', views.add_work, name='add_work'),
    path('show_work/<work_id>', views.show_work, name='show_work'),
    

]
