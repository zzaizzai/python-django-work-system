from . import views
from django.urls import path, include


urlpatterns = [
    path('all_members', views.all_members, name="all_members"),
    path('show_member/<member_id>', views.show_member, name="show_member"),
    path('login_user', views.login_user, name="login_user"),
    path('register_user', views.register_user, name="register_user"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('mypage', views.mypage, name='mypage'),
]