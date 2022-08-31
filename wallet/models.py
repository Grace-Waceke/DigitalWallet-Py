from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.forms import DateTimeField
from django.utils import timezone
# Create your models here.cxx
class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    age=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=20,null=True)
    phonenumber=models.CharField(max_length=15,null=True)
    email=models.EmailField(max_length=25,null=True)
    nationality=models.CharField(max_length=20,null=True)
    date_created=models.DateTimeField(default=timezone.now)
    profile_picture=models.ImageField(upload_to='profile_pictures/',null=True)

class Currency(models.Model):
    amount=models.IntegerField()
    country_of_origin=models.CharField(max_length=24,null=True)

class Wallet(models.Model):
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE, related_name='Wallet_currency')
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE, related_name='Wallet_customer')
    balance=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,null=True)
    # pin=models.TextField(max_length=6,null=True)

class Account(models.Model):
    account_number=models.IntegerField(default=0)
    account_type=models.CharField(max_length=20,null=True)
    balance=models.IntegerField()
    name=models.CharField(max_length=20,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name='Account_wallet')

class Transaction(models.Model):
    transaction_reference=models.CharField(max_length=200,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name='Transaction_wallet')
    actual_account=models.ForeignKey('Account',on_delete=models.CASCADE, related_name='Transaction_account')
    last_account=models.ForeignKey('Account',on_delete=models.CASCADE, related_name='Transaction_last_account')
    transaction_amount=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)

class Card(models.Model):
    card_name=models.CharField(max_length=20,null=True)
    card_number=models.IntegerField()
    security_code=models.IntegerField()
    issue_date=models.DateTimeField(default=timezone.now)
    expiry_date=models.DateTimeField(default=timezone.now)
    account=models.ForeignKey('Account',on_delete=models.CASCADE, related_name='Card_account')
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name='Card_Wallet')

class ThirdParty(models.Model):
    name=models.CharField(max_length=20,null=True)
    phonenumber=models.IntegerField()
    thirdparty_id=models.CharField(max_length=20,null=True)
    account=models.ForeignKey('Account',on_delete=models.CASCADE, related_name='ThirdParty_account')
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE, related_name='ThirdParty_currency')

class Notifications(models.Model):
    notification_id=models.CharField(max_length=25,null=True)
    date=models.DateTimeField(default=timezone.now)
    receipts= models.ForeignKey('Customer',on_delete=models.CASCADE, related_name='Notifications_receipts')

class Receipts(models.Model):
    receipt_type=models.CharField(max_length=25,null=True)
    receipt_number=models.CharField(max_length=25,null=True)
    receipt_date=models.DateTimeField(default=timezone.now)
    totalAmount=models.IntegerField(default=0)
    receiptFile=models.FileField(upload_to='wallet/')
    account=models.ForeignKey('Account',on_delete=models.CASCADE, related_name='Receipt_account')

class Loan(models.Model):
    loan_number=models.IntegerField()
    loan_type=models.CharField(max_length=25, null=True)
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Loan_wallet')
    interest_rate=models.IntegerField()
    guaranter=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Loan_guaranter')
    due_date=models.DateField(default=timezone.now)
    loan_balance=models.IntegerField()
    loan_term=models.IntegerField()
 
class Reward(models.Model):
    name=models.CharField(max_length=20,null=True)
    customer_id =models.CharField(max_length=25,null=True)
    gender= models.CharField(max_length=25,null=True)
    date=models.DateTimeField(default=timezone.now)
    bonus=models.CharField(max_length=25, null=True)
    customers=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Reward_customer')
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Reward_transaction')
















