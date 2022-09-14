# from locale import currency
from django.shortcuts import render
import wallet

from wallet.models import Customer
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipts, Reward, ThirdParty, Transaction, Wallet
from .forms import CustomerRegistrationForm, CurrencyRegistrationForm, WalletRegistrationForm, AccountRegistrationForm,TransactionRegistrationForm,CardRegistrationForm, ThirdPartyRegistrationForm, NotificationsRegistrationForm, ReceiptsRegistrationForm,LoanRegistrationForm, RewardRegistrationForm
ReceiptsRegistrationForm
# Create your views here.
def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.htm",{"form":form})

def list_customers(request):
    customers= Customer.objects.all()
    return render(request, "wallet/customers_list.htm",{"customers":customers})



def register_currency(request):
    if request.method == "POST":
        form= CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
            form = CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.htm",{"form":form})
        
def list_currencys(request):
    currencys= Currency.objects.all()
    return render(request, "wallet/currencys_list.htm",{"currencys":currencys})
        



def register_wallet(request):
    if request.method == "POST":
        form= WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.htm",{"form":form})
        
def list_wallets(request):
    wallets= Wallet.objects.all()
    return render(request, "wallet/wallets_list.htm",{"wallets": wallets})
        


def register_account(request):
    if request.method == "POST":
        form= AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AccountRegistrationForm()
    return render(request,"wallet/register_account.htm",{"form":form})
        
def list_accounts(request):
    accounts= Account.objects.all()
    return render(request, "wallet/accounts_list.htm",{"accounts": accounts})
        


def register_transaction(request):
    if request.method == "POST":
        form= TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = TransactionRegistrationForm()
    return render(request,"wallet/register_account.htm",{"form":form})
        
def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request, "wallet/transactions_list.htm",{"transactions": transactions})



def register_card(request):
    if request.method == "POST":
        
        form= CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = CardRegistrationForm()
    return render(request,"wallet/register_card.htm",{"form":form})
        
def list_cards(request):
    cards= Card.objects.all()
    return render(request, "wallet/cards_list.htm",{"cards": cards})


        
def register_thirdparty(request):
    if request.method == "POST":
        form= ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.htm",{"form":form})
        
def list_thirdpartys(request):
    thirdpartys= ThirdParty.objects.all()
    return render(request, "wallet/thirdpartys_list.htm",{"thirdpartys": thirdpartys})


        
def register_notifications(request):
    if request.method == "POST":
        form= NotificationsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = NotificationsRegistrationForm()
    return render(request,"wallet/register_notifications.htm",{"form":form})
        
def list_notification(request):
    notification= Notifications.objects.all()
    return render(request, "wallet/notification_list.htm",{"notification": notification})


    
def register_receipts(request):
    if request.method == "POST":
        form=  ReceiptsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form =  ReceiptsRegistrationForm()
    return render(request,"wallet/register_receipt.htm",{"form":form})
        
def list_receipts(request):
    receipts= Receipts.objects.all()
    return render(request, "wallet/receipts_list.htm",{"receipts": receipts})


    

def register_loan(request):
    if request.method == "POST":
        form= LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = LoanRegistrationForm()
    return render(request,"wallet/register_loan.htm",{"form":form})
        
def list_loans(request):
    loans= Loan.objects.all()
    return render(request, "wallet/loans_list.htm",{"loans": loans})

    

def register_reward(request):
    if request.method == "POST":
        form= RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = RewardRegistrationForm()
    return render(request,"wallet/register_reward.htm",{"form":form})
        
def list_rewards(request):
    rewards= Reward.objects.all()
    return render(request, "wallet/rewards_list.htm",{"rewards": rewards})

    

    