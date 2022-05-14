from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Report, Foreman


class ReportForm(forms.ModelForm):
    foremans = ((x.username, x.get_full_name()) for x in User.objects.all())
    # foremans = User.objects.all()
    # foremans = (
    #     ("t", "TEST")
    # )
    datepub = forms.DateField(label='Дата создания отчёта')
    timepub = forms.TimeField(label='Время создания отчёта', widget=forms.widgets.TimeInput())
    text = forms.CharField(label='Текст отчёта', widget=forms.widgets.Textarea())
    author = forms.ChoiceField(label="Автор", choices=foremans)

    def clean_author(self):
        username = self.cleaned_data['author']
        try:
            user = User.objects.get(username=username)
            return user
        # хз какой тут ексепшн нужно ловить
        except:
            raise ValidationError(f'Такого пользователя {username} нет в базе данных')

    class Meta:
        model = Report
        fields = ('datepub', 'timepub', 'text', "author")
