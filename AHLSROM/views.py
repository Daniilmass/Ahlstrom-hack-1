from django.shortcuts import render
from .models import *
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

