import pathlib
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

from django.http import HttpResponse
from visits.models import PageVisist


def about_view(request, *args, **kwargs):
    qs = PageVisist.objects.all()
    print(qs)
    page_qs = PageVisist.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    PageVisist.objects.create(path=request.path)
    return render(request, html_template, my_context)