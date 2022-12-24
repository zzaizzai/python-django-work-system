from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.models import User

# Create your views here.


def all_members(request):
    members = User.objects.all()
    return render(request, 'all_members.html', {"members": members})


def show_member(request, member_id):
    member = User.objects.get(pk=member_id)
    return render(request, 'show_member.html', {"member": member})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")

    form = RegisterUserForm()

    return render(request, 'register_user.html', {"form": form})


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')

        else:
            messages.success(request, ("bad login method"))
            return redirect('/members/login')

    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("logged out"))

    return redirect('home')


def mypage(request):
    return render(request, 'mypage.html', {})
