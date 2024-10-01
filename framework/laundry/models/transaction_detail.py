from django.db import models

from laundry.models import Transactions

class Transaction_details(models.Model):
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    transation_key = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)