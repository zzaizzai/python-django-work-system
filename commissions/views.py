from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Commission


def all_commissions(request):
    commissions = Commission.objects.all()
    return render(request, 'all_commissions.html', {"commissions": commissions})


def show_commission(request, commission_id):
    commission = Commission.objects.get(pk=commission_id)
    return render(request, 'show_commission.html', {"commission": commission})
