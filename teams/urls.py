from . import views
from django.urls import path, include


urlpatterns = [

    path('all_teams', views.all_teams, name="all_teams"),
    path('edit_team/<team_id>', views.edit_team, name="edit_team"),
    path('show_team/<team_id>', views.show_team, name="show_team")
]
