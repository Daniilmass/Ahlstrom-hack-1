from django.shortcuts import render
from .models import *
from . import forms
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.utils import timezone
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

import json
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

class AddSpareParts(TemplateView):
    def get(self, request):
        form = forms.Spare()
        return render(request, "add_spare_parts.html", {"form": form})


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

@csrf_exempt
def issues_add(request):
    if request.method == 'POST':
        issue_data = json.loads(request.body.decode('utf-8'))
        mach=[Machines.objects.get(name=i) for i in issue_data['machines']]
        parts=[SpareParts.objects.get(name=i) for i in issue_data['parts']]
        now = now = timezone.now()
        add_issue = Issue(injury=issue_data['injury'],fixed=issue_data['fixed'],time_not_working=now)
        add_issue.save()
        for i in mach:
            add_issue.machine_id.add(i)
        for i in parts:
            add_issue.parts_id.add(i)
        return HttpResponse(status=201)
    else:
        parts_list = SpareParts.objects.all()
        machine_list = Machines.objects.all()
        context = {'parts': parts_list, 'machine':machine_list}
        return render(request, "issue_add.html", context)

def machine_edit(request):
    return render(request, "add_news.html")

def test(request):
    news = News.objects.all().values()  # or simply .values() to get all fields
    users_list = list(news)  # important: convert the QuerySet to a list object
    return JsonResponse(users_list, safe=False)

