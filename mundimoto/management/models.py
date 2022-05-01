from django.db import models


class brands(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class versions(models.Model):
    brand = models.ForeignKey(
        "management.brands", to_field="name", db_column="brand", null=True, on_delete=models.SET_NULL)
    modelname = models.CharField(max_length=100)
    version = models.CharField(
        max_length=100, null=True, blank=True, default='')
    year = models.IntegerField()
    km = models.IntegerField()
    sell_price = models.FloatField()
    purchase_price = models.IntegerField(null=True, blank=True, default='')
