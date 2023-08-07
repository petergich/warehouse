from django.db import models
from django.core.validators import MinValueValidator
import datetime


class Purchase_Order(models.Model):
    purchase_ID = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.purchase_ID
    

class Description(models.Model):
    Description = models.CharField(max_length=50, unique=True)
    Type = models.CharField(max_length=50)
    Packaging = models.CharField(max_length=50)
    def __str__(self):
        return self.Description

class Warehouse(models.Model):
    name = models.CharField(unique=True,max_length=50)
    def __str__(self):
        return self.name



class Checkin(models.Model):
    price=models.IntegerField(blank=True,null=True)
    Quantity = models.IntegerField(validators=[MinValueValidator(0)])
    Purchase_Order = models.ForeignKey(Purchase_Order, on_delete=models.CASCADE,default=None)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    Warehouse = models.ForeignKey(Warehouse,on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return str(self.description) +" " +str(self.date)


class Returns(models.Model):
    date = models.DateField()
    material=models.ForeignKey(Description,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    returned_by = models.CharField(max_length=50)

    def __str__(self):
        return str(self.date)+" "+str(self.returned_by)


class IssuanceInternal(models.Model):
    date = models.DateField()
    material=models.ForeignKey(Description,on_delete=models.CASCADE)
    issuedTo = models.CharField(max_length=50)
    Project = models.CharField(max_length=50)
    Quantity = models.IntegerField()

    def __str__(self):
        return str(self.date)+" "+str(self.issuedTo)


class IssuanceExternal(models.Model):
    date = models.DateField()
    Purchase_order = models.ForeignKey(Purchase_Order,on_delete=models.CASCADE,null=True)
    company = models.CharField(max_length=50)
    material=models.ForeignKey(Description,on_delete=models.CASCADE)
    Carpex = models.CharField(max_length=50)
    Quantity = models.IntegerField()

    def __str__(self):
        return str(self.date)+" "+str(self.company)