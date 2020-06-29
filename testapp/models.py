from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=300)
    phone1 = PhoneNumberField()
    phone2 = PhoneNumberField(blank=True)
    email = models.EmailField()
    contact_person = models.CharField(max_length=120)
    port = models.CharField(max_length=120)


class Product(models.Model):
    name = models.CharField(max_length=120)
    data = models.CharField(max_length=120)
    certificate = models.CharField(max_length=120)
    units = models.CharField(max_length=120)


class Supplier(models.Model):
    name = models.CharField(max_length=120)
    phone = PhoneNumberField()
    email = models.EmailField()
    contact_person = models.CharField(max_length=120)
    port_of_service = models.CharField(max_length=120)
    payment_terms = models.CharField(max_length=120)


class Vessel(models.Model):
    name = models.CharField(max_length=120)
    imo_number = models.IntegerField()
    type = models.CharField(max_length=120)
    flag = models.CharField(max_length=120)
    call_sign = models.CharField(max_length=120)


class Shipowner(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = PhoneNumberField()
    email = models.EmailField()  
    contact_person = models.CharField(max_length=120)

class Broker(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = PhoneNumberField()
    email = models.EmailField()  


class Order(models.Model):
    order_date = models.DateField(auto_now=False, auto_now_add=False)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    note_for_customer = models.CharField(max_length=120)
    invoice_sent = models.BooleanField(default=False)
    currency = models.CharField(max_length=120)


class Sale(models.Model):
    port = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    delivery_date = models.DateField(auto_now=False, auto_now_add=False)
    delivery_moth = models.CharField(max_length=120)
    payment_terms = models.CharField(max_length=120)
    delivery_moth

class Bank(models.Model):
    company_name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    bank_name = models.CharField(max_length=120)
    bank_address = models.CharField(max_length=120)
    account_number= models.CharField(max_length=120)
    swift_number = models.CharField(max_length=120)
    routing_number = models.CharField(max_length=120)
    wire_transfer_number = models.CharField(max_length=120)
    currency = models.CharField(max_length=120)
    
    
