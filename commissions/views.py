from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from works.models import Work
from teams.models import Member_Team
import datetime
from .forms import CommissionForm, CommissionCommentForm
from .models import Commission, CommissionComment, CommissionHistory
# from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q


def all_commissions(request):

    sort = request.GET.get('sort', '-created_at')

    searched = request.GET.get('searched', "")

    page_limit: int = 8

    if sort == "priority":
        objss = Commission.objects.all().filter(
            Q(title__icontains=searched) |
            Q(team__name__icontains=searched) |
            Q(created_by__username__icontains=searched)

        )
        ss = sorted(objss,
                    key=lambda commission: commission.priority, reverse=True)
        p = Paginator(ss, page_limit)
    else:
        p = Paginator(Commission.objects.all().filter(
            Q(title__icontains=searched) |
            Q(team__name__icontains=searched) |
            Q(created_by__username__icontains=searched)

        ).order_by(sort), page_limit)

    # create pages
    page = request.GET.get('page')
    commissions = p.get_page(page)
    today = datetime.date.today()
    nums = "a" * commissions.paginator.num_pages

    for commission in commissions:
        if commission.date_due < today and not commission.datetime_completed:
            commission.status_due = "over"

    return render(request, 'all_commissions.html',
                  {
                      "searched": searched,
                      "sort": sort,
                      "nums": nums,
                      "commissions": commissions
                  })


def show_commission(request, commission_id):
    commission = Commission.objects.get(pk=commission_id)

    if not request.user.is_anonymous:
        CommissionHistory.objects.create(
            kind="view", parent_commission=commission, created_by=request.user)

    comments = CommissionComment.objects.filter(
        parent_commission__id=commission_id).order_by('created_at')

    form_comment = CommissionCommentForm(request.POST)

    if request.method == "POST":

        # complete commission
        if request.POST.get('complete', None):
            commission.datetime_completed = datetime.datetime.now(
                datetime.timezone.utc)
            commission.user_completed = request.user.id
            commission.save()
            CommissionHistory.objects.create(
                kind="complete", parent_commission=commission, created_by=request.user)
            return HttpResponseRedirect(f'/commissions/show_commission/{commission_id}')

        # add comment at this commission
        parent_commission = Commission.objects.get(pk=commission_id)
        if form_comment.is_valid() and not request.user.is_anonymous and parent_commission and request.POST.get('description', None):
            comment = form_comment.save(commit=False)
            comment.parent_commission = parent_commission
            comment.created_by = request.user
            comment.save()
            return HttpResponseRedirect(f'/commissions/show_commission/{commission_id}')

        messages.success(request, ("someting wrong"))

    if commission.user_completed:
        completed_by = User.objects.get(pk=commission.user_completed)
    else:
        completed_by = None

    # Check my whether it is team's work or not
    is_myteam = False
    my_teams = Member_Team.objects.filter(member__id=request.user.id)
    names_my_team = [team.team.name for team in my_teams]

    if commission.parent_work.team.name in names_my_team or commission.team.name in names_my_team:
        is_myteam = True

    histories = CommissionHistory.objects.filter(
        parent_commission__id=commission.id).exclude(kind__icontains="view").order_by('-created_at')
    return render(request, 'show_commission.html',
                  {
                      "commission": commission,
                      "completed_by": completed_by,
                      "comments": comments,
                      "form_comment": form_comment,
                      "is_myteam": is_myteam,
                      "histories": histories
                  })


def edit_commission(request, commission_id):

    commission = Commission.objects.get(pk=commission_id)
    form = CommissionForm(request.POST or None, instance=commission)

    if form.is_valid():
        form.save()
        CommissionHistory.objects.create(
            kind="edit", parent_commission=commission, created_by=request.user)
        return redirect(f'/commissions/show_commission/{commission_id}')

    return render(request, "edit_commission.html",
                  {"commission": commission,
                   "form": form})


def cancle_commission(request, commission_id):
    check_user_permission = False

    commission = Commission.objects.get(pk=commission_id)

    # the only member of wrok team can cancle chilc commission
    teams = Member_Team.objects.filter(member__id=request.user.id)
    names_of_user_team = [team.team.name for team in teams]
    if commission.parent_work.team.name in names_of_user_team:
        check_user_permission = True
    else:
        pass

    if check_user_permission:

        commission.is_cancled = True
        commission.save()
        CommissionHistory.objects.create(
            kind="cancle", parent_commission=commission, created_by=request.user)
        return redirect(f'/commissions/show_commission/{commission_id}')

    else:
        messages.success(request, ("you have no permission"))
        return redirect(f'/commissions/show_commission/{commission_id}')


def add_commission(request, work_id):

    submitted = False
    parent_work = Work.objects.get(pk=work_id)

    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission = form.save(commit=False)
            commission.created_by = request.user
            commission.parent_work = parent_work
            commission.save()
            CommissionHistory.objects.create(
                kind="add", parent_commission=commission, created_by=request.user)
        messages.success(request, ("saved commission"))
        return HttpResponseRedirect(f'/works/show_work/{work_id}')

    else:
        form = CommissionForm
        if 'sumitted' in request.GET:
            submitted = True

    form = CommissionForm(request.POST)
    return render(request, 'add_commission.html',
                  {
                      "form": form,
                      'submitted': submitted,
                      "parent_work": parent_work
                  })
