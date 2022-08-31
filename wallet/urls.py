from django .urls import path
from .views import register_account, register_card, register_currency, register_customer, register_loan, register_receipts, register_reward, register_transaction, register_wallet, register_thirdparty, register_notifications

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











]