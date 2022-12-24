from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import CommissionForm
from .models import Commission


def all_commissions(request):
    commissions = Commission.objects.all()
    return render(request, 'all_commissions.html', {"commissions": commissions})


def show_commission(request, commission_id):
    commission = Commission.objects.get(pk=commission_id)
    return render(request, 'show_commission.html', {"commission": commission})

def add_commission(request):

    submitted = False

    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.created_by = request.user
            work.save()
        return HttpResponseRedirect('/commission/add_commission?sumitted=True')
    else:
        form = CommissionForm
        if 'sumitted' in request.GET:
            submitted = True

    form = CommissionForm(request.POST)
    return render(request, 'add_commission.html', {"form": form, 'submitted': submitted})