from django.db import models

class Services(models.Model):   
    plan = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    about = models.CharField(max_length=255)
    delivery = models.BooleanField()
    
    
    def __str__(self):
        return self.id