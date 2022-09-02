from django.urls import path
from .views import notification, register_customer, reward
from .views import customer_wallet
from .views import customer_account 
from .views import transaction 
from .views import card 
from .views import thirdparty
from .views import notification
from .views import transaction_reciept
from .views import loan
from .views import reward


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
    

]