from django.contrib import admin
from bicycle_rent.models import Bicycle, Rental


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(Bicycle)
class BicycleAdmin(BaseAdmin):
    list_filter = (
        'cost',
        'number',
    )


@admin.register(Rental)
class RentalAdmin(BaseAdmin):
    list_filter = (
        'user',
        'rented_at',
    )
