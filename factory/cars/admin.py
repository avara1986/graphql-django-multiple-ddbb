# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from cars.models import Car, Model, Brand
# Register your models here.
from django.contrib import admin


class CarAdmin(admin.ModelAdmin):
    pass


class ModelAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Car, CarAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Brand, BrandAdmin)
