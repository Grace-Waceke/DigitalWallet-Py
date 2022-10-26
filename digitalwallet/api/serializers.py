from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Account, Card, Customer, Loan, Notification, Reciept, Transaction, Wallet
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "email", "age")
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("amount", "balance", "customer","pin","currency")
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_type", "account_number", "balance","description")
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_name", "card_number", "account","expiry_date","issuer","date_issued")
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("description", "date_time", "source","value","amount","status","transaction_ref","bonus_credit","origin","destination")
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("loan_term", "amount", "payment_due","loan_balance","purpose","interest_rate")
class RecieptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reciept
        fields = ("amount", "dateTime", "transaction","reciept_type","file")
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("message", "title", "status","date_time")