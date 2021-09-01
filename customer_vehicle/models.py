from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Vehicle(models.Model):
    name = models.CharField(max_length=50,blank=False, null=False, default=' ')
    make = models.CharField(max_length=20,default=' ')
    model = models.CharField(max_length=20,default=' ')
    vin_number = models.CharField(max_length=20,default=' ')
    purchase_date = models.CharField(max_length=20,default=' ')
    last_service_date = models.CharField(max_length=20,default=' ')

    class Meta:
        db_table="vehicle"

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('Client_list')
