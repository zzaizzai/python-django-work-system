from django.shortcuts import render
from .models import Work
# Create your views here.


def all_works(request):
    works = Work.objects.all()
    return render(request, 'all_works.html', {"works": works})


def show_work(request, work_id):
    work = Work.objects.get(pk=work_id)
    return render(request, 'show_work.html', {"work": work})
