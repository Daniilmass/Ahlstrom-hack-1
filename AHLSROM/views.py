from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseNotFound
import datetime

def news(request):
    news_list=News.objects.order_by('-dateTime')
    context = {'news_list': news_list}
    return render(request, 'index.html', context)

