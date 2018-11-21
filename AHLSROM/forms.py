from django import forms

from .models import *

class NewsForm(forms.Form):
    newNewsTitle = forms.CharField(label="News Title")
    newNewsText = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 10}), label="Text")
