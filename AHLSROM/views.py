from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseNotFound
import datetime

def news(request):
    news_list=News.objects.order_by('-dateTime')
    context = {'news_list': news_list}
    return render(request, 'index.html', context)

def issues(request):
    issues_list=Issue.objects.order_by('-time_not_working')
    context = {'issues_list': issues_list}
    return render(request, 'issues.html', context)

