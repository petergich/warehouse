from django.db import models
from django.core.validators import MinValueValidator
import datetime


class Purchase_Orders(models.Model):
    purchase_ID = models.CharField(max_length=50)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.purchase_ID


class SKUs(models.Model):
    Description = models.CharField(max_length=50)
    Type = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(validators=[MinValueValidator(0)])
    Packaging = models.CharField(max_length=50)
    Quantity = models.IntegerField(validators=[MinValueValidator(0)])
    Purchase_Order = models.ForeignKey(
        Purchase_Orders, on_delete=models.CASCADE)

    def __str__(self):
        return self.Description


class Capex(models.Model):
    capex_no = models.CharField(max_length=50)

    def __str__(self):
        return self.capex_no


class user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
