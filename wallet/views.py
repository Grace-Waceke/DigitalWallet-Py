from django.shortcuts import render
from .forms import CustomerRegistrationForm, CurrencyRegistrationForm, WalletRegistrationForm, AccountRegistrationForm,TransactionRegistrationForm,CardRegistrationForm, ThirdPartyRegistrationForm, NotificationsRegistrationForm, ReceiptsRegistrationForm,LoanRegistrationForm, RewardRegistrationForm
ReceiptsRegistrationForm
# Create your views here.
def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.htm",{"form":form})


def register_currency(request):
    form = CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.htm",{"form":form})

def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.htm",{"form":form})


def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.htm",{"form":form})


def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.htm",{"form":form})


def register_card(request):
    form = CardRegistrationForm()
    return render(request,"wallet/register_card.htm",{"form":form})


def register_thirdparty(request):
    form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.htm",{"form":form})


def register_notifications(request):
    form = NotificationsRegistrationForm()
    return render(request,"wallet/register_notifications.htm",{"form":form})


def register_receipts(request):
    form = ReceiptsRegistrationForm()
    return render(request,"wallet/register_receipts.htm",{"form":form})


def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,"wallet/register_loan.htm",{"form":form})


def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,"wallet/register_reward.htm",{"form":form})

