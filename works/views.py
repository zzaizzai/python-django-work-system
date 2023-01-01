from django.shortcuts import render, redirect
from .models import Work, WorkComment, WrokHistory
from django.contrib import messages
from .forms import WorkForm, WorkCommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from commissions.models import Commission
from django.db.models import Q
from teams.models import Member_Team
# Create your views here.


def all_works(request):
    searched = request.GET.get('searched', None)

    page_limit: int = 8

    if searched:

        # search title or team name or username
        p = Paginator(Work.objects.all().filter(
            Q(title__icontains=searched) |
            Q(team__name__icontains=searched) |
            Q(created_by__username__icontains=searched)
        ).order_by('-created_at'), page_limit)

    else:
        searched = ""
        p = Paginator(Work.objects.all().order_by('-created_at'), page_limit)

    page = request.GET.get('page')
    works = p.get_page(page)

    for work in works:
        commissions_of_work = Commission.objects.filter(
            parent_work__id=work.id)
        work.count_commissions = commissions_of_work.count()

    nums = "a" * works.paginator.num_pages

    return render(request, 'all_works.html',
                  {
                      "works": works,
                      "nums": nums,
                      "searched": searched
                  })


def show_work(request, work_id):

    work = Work.objects.get(pk=work_id)

    if not request.user.is_anonymous:
        WrokHistory.objects.create(
            kind="view", parent_work=work, created_by=request.user)

    form_comment = WorkCommentForm(request.POST)

    if request.method == "POST":

        parent_work = Work.objects.get(pk=work_id)

        if form_comment.is_valid() and not request.user.is_anonymousr and parent_work:
            comment = form_comment.save(commit=False)
            comment.parent_work = parent_work
            comment.created_by = request.user
            comment.save()
            return HttpResponseRedirect(f'/works/show_work/{work_id}')
        else:
            print("do nothing")
            return HttpResponseRedirect(f'/works/show_work/{work_id}')

    child_commissions = Commission.objects.filter(
        parent_work__id=work.id).order_by('-created_at')

    comments = WorkComment.objects.filter(
        parent_work__id=work.id).order_by('created_at')

    counts = {"commissions": child_commissions.count(),
              "comments": comments.count()}

    # Check my whether it is team's work or not
    is_myteam = False
    my_teams = Member_Team.objects.filter(member__id=request.user.id)
    names_my_team = [team.team.name for team in my_teams]

    if work.team.name in names_my_team:
        is_myteam = True

    # show histories of
    histories = WrokHistory.objects.filter(
        parent_work__id=work.id).exclude(kind__icontains="view").order_by('-created_at')

    return render(request, 'show_work.html',
                  {
                      "work": work,
                      "child_commissions": child_commissions,
                      "comments": comments,
                      "counts": counts,
                      "form_comment": form_comment,
                      "is_myteam": is_myteam,
                      "histories": histories
                  })


def add_work(request):

    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.created_by = request.user
            work.save()
            WrokHistory.objects.create(
                kind="add", parent_work=work, created_by=request.user)
            messages.success(request, ("added new work"))
        return HttpResponseRedirect('/works/all_works')

    form = WorkForm(request.POST)

    return render(request, 'add_work.html', {"form": form})


def edit_work(request, work_id):

    work = Work.objects.get(pk=work_id)

    form = WorkForm(request.POST or None, instance=work)

    if form.is_valid():
        form.save()
        WrokHistory.objects.create(
            kind="edit", parent_work=work, created_by=request.user)
        return redirect(f'/works/show_work/{work_id}')

    return render(request, "edit_work.html",
                  {
                      "work": work,
                      "form": form
                  })
