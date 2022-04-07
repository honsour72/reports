from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Foreman(models.Model):
    class ForemanRegions(models.TextChoices):
        adler = 'a', "Адлер"
        sochi = 's', "Сочи"
        tuapse = 't', 'Туапсе'
        lazarevskaya = 'l', 'Лазаревская'

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    region = models.CharField(max_length=1,
                              choices=ForemanRegions.choices,
                              default=ForemanRegions.adler,
                              verbose_name='Регион')

    def __str__(self):
        if self.user.username == "admin":
            return "Administrator"
        return self.user.username

    def __repr__(self):
        if self.user.username == "admin":
            return "Administrator"
        return self.user.username

    class Meta:
        # 21.03.2022 решением тверского суда деятельность компании Meta и её сервисов была признана экстремистской 😁
        verbose_name = "Данные бригадира"
        verbose_name_plural = "Данные бригадиров"


class Report(models.Model):
    author = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  verbose_name="Бригадир",
                                  )
    text = models.TextField(verbose_name="Текст отчёта")
    datepub = models.DateField(verbose_name="Дата создания отчёта")
    timepub = models.TimeField(verbose_name="Время создания отчёта")

    def __str__(self):
        return f"Отчёт:\n{self.text}\nСоздатель: {self.author}\nДата создания: {self.datepub} в {self.timepub}"

    def get_absolute_url(self):
        return f"/report/{self.pk}"

    class Meta:
        verbose_name = "Отчёт"
        verbose_name_plural = "Отчёты"
        ordering = ['datepub', 'timepub']
        unique_together = ("author", "text", "timepub")
        get_latest_by = ['datepub', 'timepub']
