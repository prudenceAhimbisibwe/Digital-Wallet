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
from .models import  Customer,Card
from .models import  Wallet
from .models import Account
from .models import Transaction
from .models import ThirdParty
from .models import Notification,Reciept,Loan,Reward

# Create your views here.
def register_customer(request):
    if request.method == 'POST':
      form=CustomerRegistrationForm(request.POST)
      if form.is_valid():
        form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"Wallet/register_customer.html",{'form':form})

def customer_wallet(request):
     if request.method == 'POST':
      form=CustomerWalletForm(request.POST)
      if form.is_valid():
        form.save()
     else:
        form=CustomerWalletForm()
     return render(request,"Wallet/customer_wallet.html",{'form':form})

def customer_account(request):
      if request.method == 'POST':
        form=CustomerAccountForm(request.POST)
        if form.is_valid():
          form.save()
      else:
         form=CustomerAccountForm()
      return render(request,"Wallet/customer_account.html",{'form':form})

def transaction(request):
     if request.method == 'POST':
        form=CustomerTransactionForm(request.POST)
        if form.is_valid():
          form.save()
     else:
        form=CustomerTransactionForm()
     return render(request,"Wallet/transaction.html",{'form':form})

def card(request):
    if request.method == 'POST':
        form=CustomerCardForm(request.POST)
        if form.is_valid():
          form.save()
    else:
       form=CustomerCardForm()
    return render(request,"Wallet/card.html",{'form':form})

def thirdparty(request):
     if request.method == 'POST':
        form=ThirdPartyForm(request.POST)
        if form.is_valid():
          form.save()
     else:
        form=ThirdPartyForm()
     return render(request,"Wallet/thirdparty.html",{'form':form})

def notification(request):
     if request.method == 'POST':
        form=CustomerNotificationForm(request.POST)
        if form.is_valid():
          form.save()
     else:
      form=CustomerNotificationForm()
     return render(request,"Wallet/notification.html",{'form':form})


def transaction_reciept(request):
     if request.method == 'POST':
        form=TransactionRecieptForm(request.POST)
        if form.is_valid():
          form.save()
     else:
      form=TransactionRecieptForm()
     return render(request,"Wallet/transaction_reciept.html",{'form':form})

def loan(request):
      if request.method == 'POST':
        form=LoanForm(request.POST)
        if form.is_valid():
          form.save()
      else:
        form=LoanForm()
      return render(request,"Wallet/loan.html",{'form':form})

def reward(request):
     if request.method == 'POST':
        form=RewardForm(request.POST)
        if form.is_valid():
          form.save()
     else:
       form=RewardForm()
     return render(request,"Wallet/reward.html",{'form':form})

# requesting all fields
def list_customers(request):
    customers=Customer.objects.all()
    return render(request,"Wallet/list_customers.html",{'customers': customers})

def list_wallets(request):
    wallets=Wallet.objects.all()
    return render(request,"Wallet/list_wallets.html",{'wallets': wallets})

def list_accounts(request):
    accounts=Account.objects.all()
    return render(request,"Wallet/list_accounts.html",{'accounts': accounts})

def list_transactions(request):
    transactions=Transaction.objects.all()
    return render(request,"Wallet/list_transactions.html",{'transactions': transactions})

def list_cards(request):
    cards=Card.objects.all()
    return render(request,"Wallet/list_cards.html",{'cards': cards})

def list_thirdparties(request):
    thirdparties=ThirdParty.objects.all()
    return render(request,"Wallet/list_thirdparties.html",{'thirdparties':thirdparties}) 

def list_notifications(request):
    notifications=Notification.objects.all()
    return render(request,"Wallet/list_notification.html",{'notifications': notifications})

def list_reciepts(request):
    reciepts=Reciept.objects.all()
    return render(request,"Wallet/list_reciepts.html",{'reciept': reciepts})

def list_loans(request):
    loans=Loan.objects.all()
    return render(request,"Wallet/list_loan.html",{'loan': loans})

def list_rewards(request):
    rewards=Reward.objects.all()
    return render(request,"Wallet/list_rewards.html",{'reward': rewards})
