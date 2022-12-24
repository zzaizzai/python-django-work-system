from django.shortcuts import render
from .models import Work
from .forms import WorkForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
# Create your views here.


def all_works(request):
    page_limit: int = 5


    p = Paginator(Work.objects.all().order_by('-created_at'), page_limit)
    page = request.GET.get('page')
    works = p.get_page(page)

    nums = "a" * works.paginator.num_pages

    return render(request, 'all_works.html',
                  {
                      "works": works,
                      "nums": nums
                  })


def show_work(request, work_id):
    work = Work.objects.get(pk=work_id)
    return render(request, 'show_work.html', {"work": work})


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
