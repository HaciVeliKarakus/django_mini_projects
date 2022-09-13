from django.contrib import admin

from apps.cars.models import Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    ...


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    ...
