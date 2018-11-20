from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import datetime

def penis(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'test.html')

def test(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'test.html')

def index(request):
    return render(request, 'index.html')

