from django.shortcuts import render
from .models import Work
# Create your views here.


def all_works(request):
    works = Work.objects.all()
    return render(request, 'all_works.html', {"works": works})
