from django.contrib import admin
from .models import Customer,Currency, Wallet, Account, Transaction, Receipts, Card, Third_party,Reward, Loan

# admin.site.register (Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phonenumber','gender','age','dob','id_number')
    search_fields=('first_name','last_name','email','phonenumber','gender','age','dob','id_number')
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Receipts)
admin.site.register(Card)
admin.site.register(Third_party)
admin.site.register(Reward)
admin.site.register(Loan)




# Register your models here.

