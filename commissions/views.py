from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from works.models import Work
import datetime
from .forms import CommissionForm
from .models import Commission
from django.http.response import JsonResponse
from django.utils import timezone


def all_commissions(request):


    commissions = Commission.objects.all().order_by('-created_at')
    today = datetime.date.today()

    for commission in commissions:
        if commission.date_due < today and not commission.datetime_completed:
            commission.status_due = "over"

    return render(request, 'all_commissions.html', {"commissions": commissions})


def show_commission(request, commission_id):
    commission = Commission.objects.get(pk=commission_id)



    if request.method == "POST":
        if request.POST.get('complete', None):
            commission.datetime_completed = datetime.datetime.now(datetime.timezone.utc)
            commission.user_completed = request.user.id
            commission.save()

    if commission.user_completed:
        completed_by = User.objects.get(pk=commission.user_completed)
    else:
        completed_by = None

    return render(request, 'show_commission.html', {"commission": commission, "completed_by":completed_by})

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
        return HttpResponseRedirect('/commissions/all_commissions')
    else:
        form = CommissionForm
        if 'sumitted' in request.GET:
            submitted = True

    form = CommissionForm(request.POST)
    return render(request, 'add_commission.html', {"form": form, 'submitted': submitted, "parent_work": parent_work})
