from django.db import models

from laundry.models import Services, Customers

class Transactions(models.Model):   
    STATUS_CHOICES = [
        ('Diambil', 'Diambil'),
        ('Proses', 'Proses'),
        ('Batal', 'Batal'),
        ('Selesai', 'Selesai'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    qty = models.IntegerField(blank=False)
    service_key = models.ForeignKey(Services, on_delete=models.CASCADE)
    customer_key = models.ForeignKey(Customers, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id