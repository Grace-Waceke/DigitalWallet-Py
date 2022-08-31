
from django import forms
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipts, Reward, Transaction, Wallet, ThirdParty
from django.forms import ModelForm

class CustomerRegistrationForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"


class CurrencyRegistrationForm(ModelForm):
    class Meta:
        model=Currency
        fields="__all__"


class WalletRegistrationForm(ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"


class AccountRegistrationForm(ModelForm):
    class Meta:
        model=Account
        fields="__all__"


class TransactionRegistrationForm(ModelForm):
    class Meta:
        model=Transaction
        fields="__all__"


class CardRegistrationForm(ModelForm):
    class Meta:
        model=Card
        fields="__all__"


class ThirdPartyRegistrationForm(ModelForm):
    class Meta:
        model= ThirdParty
        fields="__all__"


class NotificationsRegistrationForm(ModelForm):
    class Meta:
        model= Notifications
        fields="__all__"


class ReceiptsRegistrationForm(ModelForm):
    class Meta:
        model= Receipts
        fields="__all__"


class LoanRegistrationForm(ModelForm):
    class Meta:
        model= Loan
        fields="__all__"


class RewardRegistrationForm(ModelForm):
    class Meta:
        model= Reward
        fields="__all__"