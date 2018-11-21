"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AHLSROM import views
from django.conf.urls import include, url

from AHLSROM.views import AddNews

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^machines/$', views.machine, name='machine'),
    url(r'^issues/$', views.issues, name='issue'),
    url(r'^issues/add/$', views.issues_add, name='issue_add'),
    url(r'^spare_parts/$', views.parts, name='parts'),
    url(r'^issues/edit/(?P<issue_id>\w{1,50})$', views.issues_edit, name='issue_edit'),
    url(r'^machines/edit/(?P<machine_id>\w{1,50})$', views.machine_edit, name='machine_edit'),
    url(r'^spare_parts/edit/(?P<parts_id>\w{1,50})$', views.parts_edit, name='parts_edit'),
    url(r'^admin/', admin.site.urls),
    url(r'^news/add/', AddNews.as_view(), name='news/add/')
]
