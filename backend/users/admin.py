from django.contrib import admin
from users.models import CustomUser


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(CustomUser)
class CustomUserAdmin(BaseAdmin):
    list_filter = (
        'first_name',
        'email',
    )
