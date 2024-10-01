from django.db import models

from laundry.models import Services, Customers

class Transactions(models.Model):   
    STATUS_CHOICES = [
        ('Picked Up', 'Picked Up'),
        ('Process', 'Process'),
        ('Canceled', 'Canceled'),
        ('Done', 'Done'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    qty = models.IntegerField(blank=False)
    service_key = models.ForeignKey(Services, on_delete=models.CASCADE)
    customer_key = models.ForeignKey(Customers, on_delete=models.CASCADE)
    delivery = models.BooleanField()
    
    def __str__(self):
        return str(self.id)