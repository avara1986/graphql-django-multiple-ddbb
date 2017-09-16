# encoding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Car(models.Model):
    model = models.ForeignKey(
        'Model',
        on_delete=models.CASCADE,
        related_name='cars'
    )
    color = models.CharField(max_length=100, null=True)

    def __str__(self):
        return u"{} ({})".format(self.color, self.model)


@python_2_unicode_compatible
class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        related_name='models'
    )
    year = models.PositiveIntegerField(null=True)

    def __str__(self):
        return u"{} [{}-{}]".format(self.name, self.brand, self.year)


@python_2_unicode_compatible
class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return u"{}".format(self.name, )

    class Meta:
        managed = True
        db_table = 'cars_brand'
