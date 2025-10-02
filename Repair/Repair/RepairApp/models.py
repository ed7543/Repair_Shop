from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    information = models.CharField(max_length=50)

    def __str__(self):
        return self.information

class Shop(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    type = models.BooleanField(default=False) # default ne raboti na old timers
    manufacturer = models.ManyToManyField(Manufacturer)

    def __str__(self):
        return self.name

class Car(models.Model):
    type = models.CharField(max_length=10)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    color = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.type} {self.manufacturer}"


class Repair(models.Model):
    code = models.CharField(max_length=10)
    date = models.DateField()
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='repairs/')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} {self.date} {self.description} {self.car}"






