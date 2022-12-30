from . import views
from django.urls import path, include


urlpatterns = [
    path('all_commissions', views.all_commissions, name="all_commissions"),
    path('edit_commission/<commission_id>', views.edit_commission, name="edit_commission"),
    path('cancle_commission/<commission_id>', views.cancle_commission, name="cancle_commission"),
    path('add_commission/<work_id>', views.add_commission, name="add_commission"),
    path('show_commission/<commission_id>', views.show_commission, name="show_commission"),

]

