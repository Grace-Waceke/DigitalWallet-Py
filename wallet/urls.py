from django .urls import path
from .views import register_account, register_card, register_currency, register_customer, register_loan, register_receipts, register_reward, register_transaction, register_wallet, register_thirdparty, register_notifications
from . import views
urlpatterns =[
    path("register/", register_customer, name="Registration"),
    path("currency/", register_currency, name="Registration"),
    path("wallet/", register_wallet, name="Registration"),
    path("account/", register_account, name="Registration"),
    path("transaction/", register_transaction, name="Registration"),
    path("card/", register_card, name="Registration"),
    path("thirdparty/", register_thirdparty, name="Registration"),
    path("notifications/", register_notifications, name="Registration"),
    path("receipts/", register_receipts, name="Registration"),
    path("loan/", register_loan, name="Registration"),
    path("reward/", register_reward, name="Registration"),
    path("customers/", views.list_customers, name="customers_list"),
    path("currencys",views.list_currencys, name= "currencys_list"),
    path("wallets",views.list_wallets, name= "wallets_list"),
    path("accounts",views.list_accounts, name= "accounts_list"),
    path("transactions",views.list_transactions, name= "transactions_list"),
    path("cards",views.list_cards, name= "cards_list"),
    path("thirdpartys",views.list_thirdpartys, name= "thirdpartys_list"),
    path("notification",views.list_notification, name= "notification_list"),
    path("receipts",views.list_receipts, name= "receipts_list"),
    path("loans",views.list_loans, name= "loans_list"),
    path("rewards",views.list_rewards, name= "rewards_list"),



]