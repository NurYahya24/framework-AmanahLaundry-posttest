from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    adress = models.CharField(max_length=255)
    
    def __str__(self):
        
        return self.name