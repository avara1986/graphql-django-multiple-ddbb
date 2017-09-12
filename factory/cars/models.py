from django.db import models


class Car(models.Model):
    # name = models.CharField(max_length=100)
    model = models.ForeignKey(
        'Model',
        on_delete=models.CASCADE,
        related_name='cars'
    )
    color = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{} ({})".format(self.color, self.model)


class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
        related_name='models'
    )
    year = models.PositiveIntegerField(null=True)

    def __str__(self):
        return "{} [{}-{}]".format(self.name, self.brand, self.year)


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.name,)

    class Meta:
        managed = True
        db_table = 'cars_brand'
