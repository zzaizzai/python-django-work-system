from django.shortcuts import render
from .models import Team, Member_Team
from django.contrib.auth.models import User

# Create your views here.


def all_teams(request):
    teams = Team.objects.all().order_by('-id')
    for team in teams:
        num_members = Member_Team.objects.filter(team__id = team.id).count()
        team.num_members = int(num_members)
    return render(request, 'all_teams.html', {"teams": teams})


def show_team(request, team_id):
    team = Team.objects.get(pk=team_id)

    members = Member_Team.objects.filter(team_id=team.id)

    return render(request, 'show_team.html', {"team": team, "members": members})
