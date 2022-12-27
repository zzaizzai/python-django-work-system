from django.shortcuts import render, redirect
from .models import Work, WorkComment
from .forms import WorkForm, WorkCommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from commissions.models import Commission
from django.db.models import Q
# Create your views here.


def all_works(request):
    searched = request.GET.get('searched', None)

    page_limit: int = 5
    if searched:

        # search title or team name or username
        p = Paginator(Work.objects.all().filter(
            Q(title__contains=searched) |
            Q(team__name__contains=searched) |
            Q(created_by__username__contains=searched)
        ).order_by('-created_at'), page_limit)

    else:
        searched = ""
        p = Paginator(Work.objects.all().order_by('-created_at'), page_limit)

    page = request.GET.get('page')
    works = p.get_page(page)

    nums = "a" * works.paginator.num_pages

    return render(request, 'all_works.html',
                  {
                      "works": works,
                      "nums": nums,
                      "searched": searched
                  })


def show_work(request, work_id):

    form_comment = WorkCommentForm(request.POST)

    if request.method == "POST":

        parent_work = Work.objects.get(pk=work_id)

        if form_comment.is_valid() and request.user and parent_work:

            comment = form_comment.save(commit=False)
            comment.parent_work = parent_work
            comment.created_by = request.user
            comment.save()
            return HttpResponseRedirect(f'/works/show_work/{work_id}')
        else:
            print("do nothing")
            return HttpResponseRedirect(f'/works/show_work/{work_id}')

    work = Work.objects.get(pk=work_id)
    child_commissions = Commission.objects.filter(
        parent_work__id=work.id).order_by('-created_at')

    comments = WorkComment.objects.filter(
        parent_work__id=work.id).order_by('created_at')

    counts = {"commissions": child_commissions.count(),
              "comments": comments.count()}
    return render(request, 'show_work.html',
                  {"work": work,
                   "child_commissions": child_commissions,
                   "comments": comments,
                   "counts": counts,
                   "form_comment": form_comment
                   })


def add_work(request):
    submitted = False

    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.created_by = request.user
            work.save()
        return HttpResponseRedirect('/works/add_work?sumitted=True')
    else:
        form = WorkForm
        if 'sumitted' in request.GET:
            submitted = True

    form = WorkForm(request.POST)
    return render(request, 'add_work.html', {"form": form, 'submitted': submitted})


def edit_work(request, work_id):

    work = Work.objects.get(pk=work_id)

    form = WorkForm(request.POST or None, instance=work)

    if form.is_valid():
        form.save()
        return redirect(f'/works/show_work/{work_id}')

    return render(request, "edit_work.html",
                  {"work": work,
                   "form": form})
