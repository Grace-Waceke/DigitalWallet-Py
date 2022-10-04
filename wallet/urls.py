from django .urls import path
from .views import account_profile, card_profile, customer_profile, edit_account, edit_card, edit_customer, edit_receipt, edit_transaction, edit_wallet, receipt_profile, register_account, register_card, register_currency, register_customer, register_loan, register_receipts, register_reward, register_transaction, register_wallet, register_thirdparty, register_notifications, transaction_profile, wallet_profile
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
    path("customers/<int:id>/",customer_profile, name="customer_profile"),
    path("customers/edit/<int:id/", edit_customer, name="edit_customer"),
    path("wallet/<int:id>/",wallet_profile,name="wallet_profile"),
    path("wallet/edit/<int:id>/",edit_wallet,name="edit_wallet"),
    path("account/<int:id>/",account_profile,name="account_profile"),
    path("account/edit/<int:id>/",edit_account,name="edit_account"),
    path("card/<int:id>/",card_profile,name="card_profile"),
    path("card/edit/<int:id>/",edit_card,name="edit_card"),
    path("transaction/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transaction/edit/<int:id>/",edit_transaction,name="edit_transaction"),
    path("receipt/<int:id>/",receipt_profile,name="receipt_profile"),
    path("receipt/edit/<int:id>/",edit_receipt,name="edit_receipt")





]