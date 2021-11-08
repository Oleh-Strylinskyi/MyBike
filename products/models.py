from django.db import models


class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(unique=True)
    description = models.TextField(blank=True, null=True)
    country_producer = models.ForeignKey('Country', on_delete=models.SET_NULL)
    weight = models.DecimalField(decimal_places=3)
    price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
