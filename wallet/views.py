# from locale import currency
from django.shortcuts import redirect, render
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


def customer_profile(request, id):
    customer=Customer.objects.get(id=id)
    return render(request, "wallet/custoer_profile.htm", {"customer":customer})


def edit_customer(request, id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerRegistrationForm(request.POST, instance=customer)

        if form. is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id)

    else:
        form.CustomerRegistrationForm(instance=customer)
        return render(request, "wallet/edit_customer.html", {"form": form})



def wallet_profile(request, id):
    wallet=Wallet.objects.get(id=id)
    return render(request, "wallet/wallet_profile.htm", {"wallet":wallet})


def edit_wallet(request, id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST, instance=Wallet)

        if form. is_valid():
            form.save()
            return redirect("wallet_profile", id=wallet.id)

    else:
        form.WalletRegistrationForm(instance=wallet)
        return render(request, "wallet/edit_wallet.html", {"form": form})

    

def account_profile(request, id):
    account=Account.objects.get(id=id)
    return render(request, "wallet/account_profile.htm", {"account":account})


def edit_account(request, id):
    account=Account.objects.get(id=id)
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST, instance=account)

        if form. is_valid():
            form.save()
            return redirect("account_profile", id=account.id)

    else:
        form.AccountRegistrationForm(instance=account)
        return render(request, "wallet/edit_account.html", {"form": form})


   

def card_profile(request, id):
    card=Card.objects.get(id=id)
    return render(request, "wallet/card_profile.htm", {"card":card})


def edit_card(request, id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST, instance=card)

        if form. is_valid():
            form.save()
            return redirect("card_profile", id=card.id)

    else:
        form.CardRegistrationForm(instance=card)
        return render(request, "wallet/edit_card.html", {"form": form})

                

  

def transaction_profile(request, id):
    transaction=Transaction.objects.get(id=id)
    return render(request, "wallet/transaction_profile.htm", {"transaction":transaction})


def edit_transaction(request, id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST, instance=transaction)

        if form. is_valid():
            form.save()
            return redirect("card_profile", id=transaction.id)

    else:
        form.TransactionRegistrationForm(instance=transaction)
        return render(request, "wallet/edit_transaction.html", {"form": form})


def transaction_profile(request, id):
    transaction=Transaction.objects.get(id=id)
    return render(request, "wallet/transaction_profile.htm", {"transaction":transaction})


def edit_transaction(request, id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=TransactionRegistrationForm(request.POST, instance=transaction)

        if form. is_valid():
            form.save()
            return redirect("card_profile", id=transaction.id)

    else:
        form.TransactionRegistrationForm(instance=transaction)
        return render(request, "wallet/edit_transaction.html", {"form": form})

                
       
def receipt_profile(request, id):
    receipt=Receipts.objects.get(id=id)
    return render(request, "wallet/receipt_profile.htm", {"receipt":receipt})

def edit_receipt(request, id):
    receipt=Receipts.objects.get(id=id)
    if request.method=="POST":
        form=ReceiptsRegistrationForm(request.POST, instance=receipt)

        if form. is_valid():
            form.save()
            return redirect("card_profile", id=receipt.id)

    else:
        form.ReceiptsRegistrationForm(instance=receipt)
        return render(request, "wallet/edit_receipt.html", {"form": form})

                
    

    
                
    

    