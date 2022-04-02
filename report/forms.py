from django import forms
from django.forms import widgets

from .models import Reports


class ReportsForm(forms.ModelForm):
    text = forms.Textarea()
    datepub = forms.DateTimeField()

    class Meta:
        model = Reports
        fields = ("datepub", "text", "author")
