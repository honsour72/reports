from django.db import models
from django.contrib.auth.models import User


regions = (
    ('Адлер', 'АДЛЕР'),
    ('Сочи', 'СОЧИ'),
    ('Туапсе', 'ТУАПСЕ'),
    ('Лазаревская', 'ЛАЗАРЕВСКАЯ'),
)


# Create your models here.
# отчет
class UserRegion(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    region = models.CharField(max_length=15, choices=regions, default='Адлер')

    def __unitcode__(self):
        return self.user

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Reports(models.Model):
    author = models.CharField(max_length=25)
    text = models.TextField()
    datepub = models.DateTimeField(editable=True)

    def __str__(self):
        return f'{self.datepub} | {self.author} - {self.text}'

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'


# CASCADE: когда объект, на который имеется ссылка,
# удаляется, все объекты, ссылающиеся на этот объект, также будут удалены.
# промежуточная модель
# class Membership(models.Model):
#     reports = models.ForeignKey(Reports, on_delete=models.CASCADE)
