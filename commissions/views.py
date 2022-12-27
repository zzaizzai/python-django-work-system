from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from works.models import Work
import datetime
from .forms import CommissionForm
from .models import Commission, CommissionComment
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.utils import timezone


def all_commissions(request):

    page_limit: int = 5

    # commissions = Commission.objects.all().order_by('-created_at')

    p = Paginator(Commission.objects.all().order_by('-created_at'), page_limit)

    page = request.GET.get('page')
    commissions = p.get_page(page)

    today = datetime.date.today()

    nums = "a" * commissions.paginator.num_pages

    for commission in commissions:
        if commission.date_due < today and not commission.datetime_completed:
            commission.status_due = "over"

    return render(request, 'all_commissions.html',
                  {
                      "nums": nums,
                      "commissions": commissions})


def show_commission(request, commission_id):
    commission = Commission.objects.get(pk=commission_id)

    comments = CommissionComment.objects.filter(
        parent_commission__id=commission_id).order_by('created_at')

    if request.method == "POST":
        if request.POST.get('complete', None):
            commission.datetime_completed = datetime.datetime.now(
                datetime.timezone.utc)
            commission.user_completed = request.user.id
            commission.save()

    if commission.user_completed:
        completed_by = User.objects.get(pk=commission.user_completed)
    else:
        completed_by = None

    return render(request, 'show_commission.html',
                  {
                      "commission": commission,
                      "completed_by": completed_by,
                      "comments": comments
                  })


def edit_commission(request, commission_id):

    commission = Commission.objects.get(pk=commission_id)

    form = CommissionForm(request.POST or None, instance=commission)

    if form.is_valid():
        form.save()
        return redirect(f'/commissions/show_commission/{commission_id}')

    return render(request, "edit_commission.html",
                  {"commission": commission,
                   "form": form})


def complete_commission(request):
    # return
    return JsonResponse("ddd")


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
        messages.success(request, ("saved commission"))
        return HttpResponseRedirect(f'/works/show_work/{work_id}')

    else:
        form = CommissionForm
        if 'sumitted' in request.GET:
            submitted = True

    form = CommissionForm(request.POST)
    return render(request, 'add_commission.html', {"form": form, 'submitted': submitted, "parent_work": parent_work})
