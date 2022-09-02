from django.shortcuts import render
from .forms import CustomerRegistrationForm
from .forms import CustomerWalletForm
from .forms import CustomerAccountForm
from .forms import CustomerTransactionForm
from .forms import CustomerCardForm
from .forms import ThirdPartyForm
from .forms import CustomerNotificationForm
from .forms import TransactionRecieptForm
from .forms import LoanForm
from .forms import  RewardForm

# Create your views here.
def register_customer(request):
    form=CustomerRegistrationForm()
    return render(request,"Wallet/register_customer.html",{'form':form})

def customer_wallet(request):
    form=CustomerWalletForm()
    return render(request,"Wallet/customer_wallet.html",{'form':form})

def customer_account(request):
    form=CustomerAccountForm()
    return render(request,"Wallet/customer_account.html",{'form':form})

def transaction(request):
    form=CustomerTransactionForm()
    return render(request,"Wallet/transaction.html",{'form':form})

def card(request):
    form=CustomerCardForm()
    return render(request,"Wallet/card.html",{'form':form})

def thirdparty(request):
    form=ThirdPartyForm()
    return render(request,"Wallet/thirdparty.html",{'form':form})

def notification(request):
    form=CustomerNotificationForm()
    return render(request,"Wallet/notification.html",{'form':form})


def transaction_reciept(request):
    form=TransactionRecieptForm()
    return render(request,"Wallet/transaction_reciept.html",{'form':form})

def loan(request):
    form=LoanForm()
    return render(request,"Wallet/loan.html",{'form':form})

def reward(request):
    form=RewardForm()
    return render(request,"Wallet/reward.html",{'form':form})



