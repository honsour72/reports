from django.db import models
from django.contrib.auth.models import User

regions = (
    ("Аддер", "Адлер"),
    ("Сочи", "СОЧИ"),
    ("Туапсе", "ТУАПСЕ"),
    ("Лазаревская", "ЛАЗАРЕВСКАЯ"),
)


# Create your models here.

class UserRegion(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    region = models.CharField(max_length=15, choices=regions, default='Адлер')

    def _＿str＿_(self):
        return self.user

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Reports(models.Model):
    author = models.CharField(max_length=25)
    text = models.TextField()
    datepub = models.DateTimeField(editable=True)

    def _＿str_＿(self):
        return f'{self.datepub} | {self.author} - {self.text}'

    class Meta:
        verbose_name = "Отчёт"
        verbose_name_plural = 'Отчёты'
