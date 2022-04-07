from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Foreman, Report


class ForemanInline(admin.StackedInline):
    model = Foreman
    can_delete = True
    verbose_name_plural = "Данные бригадира"


class UserAdmin(UserAdmin):
    inlines = (ForemanInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Report)

