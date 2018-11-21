from django.shortcuts import render
from .models import *
from . import forms
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseNotFound
import datetime

def issues_edit(request,issue_id):
    issue = Issue.objects.get(id=int(issue_id))
    context = {'issue_data': issue}
    return render(request, 'issue_edit.html', context)

def news(request):
    news_list=News.objects.order_by('-dateTime')
    context = {'news_list': news_list}
    return render(request, 'index.html', context)

#TODO: Сдлать обработку duration fix
def issues(request):
    issues_list=Issue.objects.order_by('-time_not_working')
    context = {'issues_list': issues_list}
    return render(request, 'issues.html', context)

def newsAdd(request):
        return render(request, "add_news.html")


class AddNews(TemplateView):
    def get(self, request):
        form = forms.NewsForm()
        return render(request, "add_news.html", {"form": form})


def parts(request):
    parts_list = SpareParts.objects.order_by('-name')
    context = {'parts_list': parts_list}
    return render(request, "parts.html",context)

def machine(request):
    return render(request, "add_news.html")

def parts_edit(request,parts_id):
    parts_list = SpareParts.objects.get(id=parts_id)
    context = {'parts': parts_list}
    return render(request, "parts_edit.html", context)

def machine_edit(request):
    return render(request, "add_news.html")



