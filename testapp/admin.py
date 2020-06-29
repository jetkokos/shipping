from django.contrib import admin
from testapp.models import Agent, Product, Supplier, Vessel, Shipowner, Broker, Order, Bank, Sale

# Register your models here.

admin.site.register(Agent)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Vessel)
admin.site.register(Shipowner)
admin.site.register(Broker)
admin.site.register(Order)
admin.site.register(Bank)
admin.site.register(Sale)