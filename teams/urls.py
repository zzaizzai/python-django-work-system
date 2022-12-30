from . import views
from django.urls import path, include


urlpatterns = [

    path('all_teams', views.all_teams, name="all_teams"),
    path('show_team/<team_id>', views.show_team, name="show_team")
]
