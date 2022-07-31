
from datetime import datetime
import email
from pyexpat import model
from random import choices
from _tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.utils import timezone
from turtle import title

# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    age=models.CharField(max_length=10,null=True)
    address=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=25,null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    id_number =models.CharField(max_length=25)
    dob =models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    nationality=models.CharField(max_length=20,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)

class Currency(models.Model):
    amount=models.IntegerField()
    country_of_origin=models.CharField(max_length=24,null=True) 


class Wallet(models.Model):
    fcurrency =models.ForeignKey(Currency, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    balance=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,null=True)
    pin=models.TextField(max_length=6,null=True)

class Account(models.Model):
    account_number=models.IntegerField()
    account_type=models.CharField(max_length=20,null=True)
    balance=models.IntegerField()
    name=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)

class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=255,null=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    transaction_amount=models.IntegerField()
    TRANSACTION_TYPES= (
        ('w', 'withdrawal'),
        ('d', 'deposit'),
    )
    transaction_type=models.CharField(max_length=1, choices=TRANSACTION_TYPES,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    # Receipt=models.OneToOneField(null=True)
    # Original_account=models.ForeignKey(Account, on_delete=models.CASCADE)
    # Destination_account=models.ForeignKey(Account, on_delete=models.CASCADE)


class Receipts(models.Model):
    receipt_type=models.CharField(max_length=25, null=True)
    receipt_date=models.DateTimeField(default=timezone.now)
    recipt_number=models.CharField(max_length=25, null=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    total_Amount=models.IntegerField()
    transaction=models.ForeignKey(Transaction, on_delete=models.CASCADE)
    recipt_File=models.FileField(upload_to='wallet/')


class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=20,null=True)
    card_number=models.IntegerField()
    ISSUER=(
        'mastercard'
        'visacard'
    )
    card_type=models.CharField(max_length=200)
    expiry_date=models.DateTimeField(default='')
    cardstate=(
        'd','debit',
        'c','credit',
    )
    card_status=models.CharField(max_length=200)
    cVV_Security=models.IntegerField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)


class Third_party(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    name=models. CharField(max_length=15,null=True)
    Third_id=models.CharField(max_length=10,null=True)
    phone_Number=models.IntegerField()
    currency=models.ForeignKey(Currency,on_delete=models.CASCADE)

class Reward(models.Model):
    name =models.CharField(max_length=15,null=True)
    customer_id =models.IntegerField()
    transactions =models.ForeignKey(Transaction,on_delete=models.CASCADE)
    points =models.IntegerField()
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    datetime =models.DateTimeField(default=timezone.now)
    Receipts =models.ForeignKey(Customer,on_delete=models.CASCADE)


class Loan(models.Model):
    loan_number =models.IntegerField()
    loan_type =models.CharField(max_length=25)
    amount =models.IntegerField()
    # Wallet =models.ForeignKey()
    datetime =models.DateTimeField(default=timezone.now)
    loan_term =models.IntegerField(max_length=30)
    payment_due_date =models.DateTimeField()
    guaranter =models.ForeignKey(Customer,on_delete=models.CASCADE)
    interest_rate =models.IntegerField()


class Notification(models.Model):
    message =models.CharField(max_length=50, null=True)
    title =models.CharField(max_length=50,null=True)
    date_time =models.DateTimeField(default=timezone.now)
    email =models.EmailField()
    status =models.CharField(max_length=30)
    



    
    

    
    


