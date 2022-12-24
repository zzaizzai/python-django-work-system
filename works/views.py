from django.shortcuts import render
from .models import Work
from .forms import WorkForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


def all_works(request):
    works = Work.objects.all()
    return render(request, 'all_works.html', {"works": works})


def show_work(request, work_id):
    work = Work.objects.get(pk=work_id)
    return render(request, 'show_work.html', {"work": work})


def add_work(request):
    submitted = False

    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/works/add_work?sumitted=True')
    else:
        form = WorkForm
        if 'sumitted' in request.GET:
            submitted = True

    form = WorkForm(request.POST)
    return render(request, 'add_work.html', {"form": form, 'submitted': submitted})
