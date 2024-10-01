from django.db import models

class Services(models.Model):   
    plan = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    about = models.CharField(max_length=255)
    max_load = models.IntegerField(blank=False)
    
    
    def __str__(self):
        return str(self.id)