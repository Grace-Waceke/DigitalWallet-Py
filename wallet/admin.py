from django.contrib import admin
from .models import Customer, Notifications,Wallet,Currency,Transaction,Card,ThirdParty ,Receipts,Loan,Reward,Account
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)

class ReceiptsAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_date','account','totalAmount')
    search_fields=('receipt_date','receipt_date',)
admin.site.register(Receipts,ReceiptsAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_reference','transaction_amount','transaction_date')
    search_fields=('transaction_reference','transaction_amount','transaction_date')
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=('card_name','card_number')
    search_fields=('card_name','card_number')
admin.site.register(Card, CardAdmin)

class Third_partyAdmin(admin.ModelAdmin):
    list_display=('account','thirdparty_id','phonenumber','currency')
    search_fields=('account','thirdparty_id','phonenumber','currency')
admin.site.register(ThirdParty,Third_partyAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=('amount','country_of_origin')
    search_fields=('amount','country_of_origin')
admin.site.register(Currency,CurrencyAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=('customer','balance','amount','date','status')
    search_fields=(' currency','customer','balance','amount','date','status')
admin.site.register(Wallet,WalletAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=('transaction','date','customer','gender','bonus')
    search_fields=('transaction','date','customer','gender','bonus')
admin.site.register(Reward,RewardAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_number','loan_type','amount','date')
    search_fields=('loan_number','loan_type')
admin.site.register(Loan,LoanAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display=('notification_id','date', 'receipts')
    search_fields=('notification_id','date', 'receipts')
admin.site.register(Notifications,NotificationsAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_number', 'account_type','balance','name')
    search_fields=('account_number', 'account_type')
admin.site.register(Account,AccountAdmin)