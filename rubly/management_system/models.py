from django.db import models
from django.core.validators import MinValueValidator
import datetime


class Purchase_Order(models.Model):
    purchase_ID = models.CharField(max_length=50)

    def __str__(self):
        return self.purchase_ID
    

class Description(models.Model):
    Description = models.CharField(max_length=50)
    Type = models.CharField(max_length=50, null=True, blank=True)
    Packaging = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Warehouse(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name



class Checkin(models.Model):
    Quantity = models.IntegerField(validators=[MinValueValidator(0)])
    Purchase_Order = models.ForeignKey(Purchase_Order, on_delete=models.CASCADE,null=True)
    Description = models.ForeignKey(Description, on_delete=models.CASCADE)
    Warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Description) + str(self.Warehouse)


class Returns(models.Model):
    date = models.DateField()
    material=models.ForeignKey(Description,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    rteurned_by = models.CharField(max_length=50)

    def _str_(self):
        return self.date


class IssuanceInternal(models.Model):
    date = models.DateField()
    material=models.ForeignKey(Description,on_delete=models.CASCADE)
    issuedTo = models.CharField(max_length=50)
    Project = models.CharField(max_length=50)
    Quantity = models.IntegerField()

    def _str_(self):
        return self.issuedTo


class IssuanceExternal(models.Model):
    date = models.DateField()
    Purchase_order = models.ForeignKey(Purchase_Order,on_delete=models.CASCADE,null=True)
    company = models.CharField(max_length=50)
    material=models.ForeignKey(Description,on_delete=models.CASCADE)
    Carpex = models.CharField(max_length=50)
    Quantity = models.IntegerField()

    def _str_(self):
        return self.company