from django import forms

from .models import *

class NewsForm(forms.Form):
    newNewsTitle = forms.CharField(label="News Title")
    newNewsText = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 10}), label="Text")

class SparePartsForm(forms.Form):
    newSparePartName = forms.CharField(label="Spare Part Name")
    newSparePartNumber = forms.IntegerField()