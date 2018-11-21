from django.db import models

# Create your models here.

class News(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=200)
    dateTime = models.DateTimeField()
    topic = models.CharField(max_length=60)

class SpareParts(models.Model):
    id = models.AutoField(primary_key=True)
    counter = models.IntegerField()
    name = models.CharField(max_length=60)
    date_usage = models.DateTimeField(blank=True,null=True)


class Machines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    parts = models.ManyToManyField(SpareParts)
    previous_fix_time = models.DateTimeField(blank=True,null=True)

class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    parts_id = models.ManyToManyField(SpareParts)

class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    machine_id = models.ManyToManyField(Machines)
    parts_id = models.ManyToManyField(SpareParts)
    time_not_working = models.DateTimeField()
    injury = models.BooleanField(default=False)
    fixed = models.BooleanField(default=False)
    duration_unfix=models.IntegerField(null=True,blank=True)