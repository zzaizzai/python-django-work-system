from . import views
from django.urls import path, include


urlpatterns = [
    path('all_commissions', views.all_commissions, name="all_commissions"),
    path('add_commission', views.add_commission, name="add_commission"),
    path('show_commission/<commission_id>', views.show_commission, name="show_commission"),

]

