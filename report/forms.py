from django import forms
from django.forms import widgets

from .models import Reports


class ReportsForm(forms.ModelForm):
    text = forms.Textarea()
    datepub = forms.DateTimeField()
    # author = forms.CharField(widget=forms.Select(author="user"))
    # author = forms.TextInput(attrs={'title': 'Ivan'})
    # author = forms.Textarea()
    # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=author)
    class Meta:
        model = Reports
        fields = ("datepub", "text", "author")

    # class ReadOnlyWidget(widgets.Widget):
    #     model = Reports
    #     fields = ("datepub", "text", "author")
