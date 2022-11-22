from django.shortcuts import render,redirect
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

# accessing a single customer
def customer_profile(request,id):
    customers=Customer.objects.get(id=id)
    return render(request,"Wallet/customer_profile.html",{'customer':customers})

# update customer_profile
def edit_profile(request,id):
  customers = Customer.objects.get(id=id)
  if request.method == 'POST':
    form=CustomerRegistrationForm(request.POST, instance=customers)
    if form.is_valid():
      form.save()
    return redirect("customer_profile", id=customers)
  else:
    form = CustomerRegistrationForm(instance=customers)
    return render(request,"wallet/edit_profile.html",{"form": form})

# Single wallet profile
def wallet_profile(request,id):
   wallets=Wallet.objects.get(id=id)
   return render(request,"Wallet/wallet_profile.html",{'wallet':wallets})

# update wallet profile
def editWallet_profile(request,id):
  wallets = Wallet.objects.get(id=id)
  if request.method == 'POST':
    form=CustomerWalletForm()(request.POST, instance=wallets)
    if form.is_valid():
      form.save()
    return redirect("wallet_profile", id=wallets)
  else:
    form = CustomerWalletForm()(instance=wallets)
    return render(request,"wallet/editWallet_profile.html",{"form": form})

def wallet_profile(request,id):
   wallets=Wallet.objects.get(id=id)
   return render(request,"Wallet/wallet_profile.html",{'wallet':wallets})


# Single account profile
def wallet_profile(request,id):
   accounts=Account.objects.get(id=id)
   return render(request,"Wallet/account_profile.html",{'account':accounts})

# update account profile
def editAccount_profile(request,id):
  accounts = Account.objects.get(id=id)
  if request.method == 'POST':
    form=CustomerAccountForm()(request.POST, instance=accounts)
    if form.is_valid():
      form.save()
    return redirect("account_profile", id=accounts)
  else:
    form = CustomerAccountForm()(instance=accounts)
    return render(request,"wallet/editWallet_profile.html",{"form": form})

def wallet_profile(request,id):
   accounts=Account.objects.get(id=id)
   return render(request,"Wallet/account_profile.html",{'accounts':accounts})

# Single card profile
def card_profile(request,id):
   cards=Card.objects.get(id=id)
   return render(request,"Wallet/card_profile.html",{'cards':cards})

# update card profile
def editCard_profile(request,id):
  cards = Card.objects.get(id=id)
  if request.method == 'POST':
    form=CustomerCardForm()(request.POST, instance=cards)
    if form.is_valid():
      form.save()
    return redirect("card_profile", id=cards.id)
  else:
    form = CustomerCardForm()(instance=cards)
    return render(request,"wallet/editCard_profile.html",{"form": form})

# Single transaction profile
def transaction_profile(request,id):
   transactions=Transaction.objects.get(id=id)
   return render(request,"Wallet/transaction_profile.html",{'transctions':transactions})

# update transaction profile
def editTransction_profile(request,id):
  transactions = Transaction.objects.get(id=id)
  if request.method == 'POST':
    form=CustomerTransactionForm()(request.POST, instance=transactions)
    if form.is_valid():
      form.save()
    return redirect("transaction_profile", id=transactions.id)
  else:
    form = CustomerTransactionForm()(instance=transactions)
    return render(request,"wallet/editTransaction_profile.html",{"form": form})
