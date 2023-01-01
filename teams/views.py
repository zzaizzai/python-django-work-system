from django.shortcuts import render
from .models import Team, Member_Team
from django.contrib.auth.models import User
from .forms import TeamMemberForm
from django.contrib import messages

# Create your views here.


def all_teams(request):
    teams = Team.objects.all().order_by('-id')
    for team in teams:
        num_members = Member_Team.objects.filter(team__id=team.id).count()
        team.num_members = int(num_members)
    return render(request, 'all_teams.html',
                  {
                      "teams": teams
                  })


def show_team(request, team_id):
    team = Team.objects.get(pk=team_id)

    members = Member_Team.objects.filter(team_id=team.id)

    return render(request, 'show_team.html',
                  {
                      "team": team,
                      "members": members
                  })


def edit_team(request, team_id):

    team = Team.objects.get(pk=team_id)

    members = Member_Team.objects.filter(team_id=team.id)
    form = TeamMemberForm(request.POST)

    member_new_id = request.POST.get('member', None)
    if member_new_id:
        form = TeamMemberForm()
        member_new = User.objects.get(pk=member_new_id)
        member_check = Member_Team.objects.filter(member__id=member_new.id, team__id=team_id).first()

        if not member_check:
            # create new member 
            Member_Team.objects.create(member=member_new, team=team)
            
        else:
            messages.success(request, ("already exist"))


    return render(request, 'edit_team.html',
                  {
                      "team": team,
                      "members": members,
                      "form": form
                  })
