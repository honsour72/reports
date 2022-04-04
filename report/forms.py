from django import forms
from django.forms import widgets

from .models import Reports


class ReportsForm(forms.ModelForm):
    text = forms.Textarea()
    # datepub = forms.DateTimeField()
    datepub = forms.SelectDateWidget()
    r = Reports.objects.all()
    author = forms.Select(choices=list(set([x.author for x in r])))

    class Meta:
        model = Reports
        fields = ("datepub", "text", "author")
