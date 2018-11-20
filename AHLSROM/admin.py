from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import News, SpareParts, Machines, Warehouse, Issue

admin.site.register(SpareParts)
admin.site.register(Machines)
admin.site.register(News)
admin.site.register(Warehouse)
admin.site.register(Issue)