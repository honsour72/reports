from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserRegion, Reports


class UserInline(admin.StackedInline):
    model = UserRegion
    can_delete = False
    verbose_name_plural = 'регион'


class UserAdmin(UserAdmin):
    inlines = (
        UserInline,
    )


admin.site.unregister(User)
admin.site.register(Reports)
admin.site.register(User, UserAdmin)
