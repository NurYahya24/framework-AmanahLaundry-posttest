from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Customers, Services, Transactions, Transaction_details as td
# Register your models here.


class detailedTransactions(admin.ModelAdmin):
    list_display = ('status', 'qty', 'delivery')
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        
        service = obj.service_key
        qty = obj.qty
        delivery = obj.delivery
        
        total_price = service.price * qty
        if delivery:
            total_price += 5000 
            
        td.objects.create(
            transation_key=obj,
            total_price=total_price,
        )

admin.site.register(Customers)
admin.site.register(Services)
admin.site.register(Transactions, detailedTransactions)
admin.site.register(td)