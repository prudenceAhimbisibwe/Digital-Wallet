from django.urls import path
from .views import  notification, register_customer, reward
from .views import customer_wallet
from .views import customer_account 
from .views import transaction 
from .views import card 
from .views import thirdparty
from .views import notification
from .views import transaction_reciept
from .views import loan
from .views import reward
from .views import list_customers
from .views import list_wallets
from .views import list_accounts
from .views import list_transactions
from .views import list_cards
from .views import list_thirdparties
from .views import list_notifications
from .views import list_reciepts
# from .views import list_loans
# from .views import list_rewards




# creating a path
urlpatterns =[
    path("register/",register_customer,name="registration"),
    path("customer/",customer_wallet,name="customer_wallet"),
    path("account/",customer_account,name="customer_account"),
    path("transaction/",transaction,name="transaction"),
    path("card/",card,name="card"),
    path("thirdparty/",thirdparty,name="thirdparty"),
    path("notification/",notification,name="customer_notification"),
    path("reciept/",transaction_reciept,name="transaction_reciept"),
    path("loan/",loan,name="loan"),
    path("reward/",reward,name="reward"),
    path("customers/",list_customers,name="customers"),
    path("accounts/",list_accounts,name="account_list"),
    path("wallets/",list_wallets,name="wallet_list"),
    path("transactions/",list_transactions,name="transaction_list"),
    path("cards/",list_cards,name="card_list"),
    path("thirdparties/",list_thirdparties,name="thirdparty_list"),
    path("notifications/",list_notifications,name="notification_list"),
    path("reciepts/",list_reciepts,name="receipts_list"),
#     path("loans/",list_loans,name="loans_list"),
#     path("rewards/",list_rewards,name="rewards_list"),   
]
