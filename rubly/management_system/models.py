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

class Client(models.Model):
    name = models.CharField(unique=True,max_length=50)
    def __str__(self):
        return self.name
class Owner(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField(max_length=254)


    def __str__(self):
        return self.name
class Project_Type(models.Model):
    name=models.CharField(max_length=254)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    owner=models.ForeignKey(Owner,on_delete=models.SET_NULL,null=True)
    class Meta:
        # Specify the unique_together constraint
        unique_together = ['client', 'name']
    def __str__(self):
        return "Client:"+" "+self.client.name+" "+"Name:"+" "+self.name

class Goods_received(models.Model):
    price=models.IntegerField(blank=True,null=True)
    Quantity = models.IntegerField(validators=[MinValueValidator(0)])
    Project_Type=models.ForeignKey(Project_Type,on_delete=models.SET_NULL,null=True)
    Purchase_Order = models.ForeignKey(Purchase_Order, on_delete=models.CASCADE,default=None)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    date=models.DateField()
    remaining=models.IntegerField()
    def save(self, *args, **kwargs):
        # Set remaining to the same value as Quantity if not provided
        if self.remaining is None:
            self.remaining = self.Quantity
        super().save(*args, **kwargs)
    class Meta:
        # Specify the unique_together constraint
        unique_together = ['Purchase_Order', 'description']
    def __str__(self):
        return "PO:"+str(self.Purchase_Order.purchase_ID)+", "+"Good:"+str(self.description)


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
class Project(models.Model):
    project_type=models.ForeignKey(Project_Type,on_delete=models.CASCADE)
    region=models.CharField(max_length=100)

    def __str__(self):
        return self.project_type.name +" "+self.region
    



