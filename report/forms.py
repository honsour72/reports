from django import forms
from .models import Reports


class ReportsForm(forms.ModelForm):
    text = forms.Textarea()
    datepub = forms.DateTimeField()
    # author = forms.TextInput(
    #     widget=forms.widgets.Select(attrs={'value':'Ivan'})
    # )

    class Meta:
        model = Reports
        fields = ("datepub", "text", "author")

