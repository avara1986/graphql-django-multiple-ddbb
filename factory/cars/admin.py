from django.contrib import admin

# Register your models here.
from django.contrib import admin
from cars.models import Car, Model, Brand


class CarAdmin(admin.ModelAdmin):
    pass


class ModelAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Brand, BrandAdmin)
