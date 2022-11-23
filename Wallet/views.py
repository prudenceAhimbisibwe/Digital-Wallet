from django.shortcuts import render,redirect
from django.views.generic.base import View
from email import message
from .forms import *
from rest_framework import views
from rest_framework.response import Response

# Create your views here
def home_page(request):
    return render(request,"Wallet/index.html")

def register_customer(request):
    if request.method=='POST':
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegistrationForm()
    return render(request,"Wallet/register_customer.html",{"form":form})

def customer_profile(request,id):
   customers=Customer.objects.get(id=id)
   return render(request,"Wallet/customer_profile.html",{"customers":customers })
def edit_customer(request,id):
   customer=Customer.objects.get(id=id)
   if request.method =='POST':
       form=CustomerRegistrationForm(request.POST,instance=customer)
       if form.is_valid():
           form.save()
           return redirect("customerProfile",id=customer.id)
   else:
       form=CustomerRegistrationForm(instance=customer)
   return render(request,"Wallet/edit_customer.html",{"forms":form})

class SearchCustomer(View):
    model = Customer
    template_name = 'Wallet/list_customers.html'

    def get(self,request):
        customers=Customer.objects.all()
        customer_found=request.GET.get('customer_found',None)     #request takes form as customer_found 
        if customer_found:
            result=Customer.objects.filter(first_name__contains=customer_found)    #filter from database and assign it tothe request 
            context={'Customers':result}
            return render(request, self.template_name,context)   #return result
        context={'Customers':customers}
        return render(request, self.template_name,context)                                  

def register_account(request):
    if request.method=="POST":
            form_account=CustomerAccountForm(request.POST)
            if form_account.is_valid():
                form_account.save()
    else:
        form_account=CustomerAccountForm()
    return render(request,'Wallet/list_accounts.html',{"form":form_account} )

def list_accounts(request):
    accounts=Account.objects.all()
    return render(request,'Wallet/list_accounts.html',{
        "accounts":accounts})

def account_profile(request,id):
    account=Account.objects.get(id=id)
    return render(request,"Wallet/account_profile.html",{"accounts":account})

def edit_account(request,id):
    account=Account.objects.get(id=id)
    if request.method == "POST":
        form=CustomerAccountForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect("accountProfile",id=account.id)
    else:
        form=CustomerAccountForm(instance=account)
    return render(request,"Wallet/edit_account.html",{"forms":form})

def register_wallet(request):
    if request.method=="POST":
            form_wallet=CustomerWalletForm(request.POST)
            if form_wallet.is_valid():
                form_wallet.save()
    else:
        form_wallet=CustomerWalletForm()
    return render(request,"Wallet/customer_wallet.html", {"wallet":form_wallet} )

def wallet_profile(request,id):
    wallet=Wallet.objects.get(id=id)
    return render(request,"Wallet/account_profile.html",{"wallets":wallet})
def edit_wallet(request,id):
    wallet=Wallet.objects.get(id=id)
    if request.method=="POST":
        form=CustomerWalletForm(request.POST,instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("walletProfile",id=wallet.id)
    else:
        form=CustomerWalletForm(instance=wallet)
        return render(request,"Wallet/edit_wallet.html",{"forms":form})


def list_wallet(request):
    wallet=Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",{"wallet":wallet})

def register_transaction(request):
    if request.method=="POST":
            form_transact=CustomerTransactionForm(request.POST)
            if form_transact.is_valid():
                form_transact.save()
    else:
        form_transact=CustomerTransactionForm()
    return render(request,"Wallet/register_transaction.html", {"transact":form_transact})

def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"Wallet/transaction_list.html",{"transactions":transactions})

def register_card(request):
    card_form=CustomerCardForm()
    if request.method=="POST":
        card_form=CustomerCardForm(request.POST)
        if card_form.is_valid():
            card_form.save()
    else:
        card_form=CustomerCardForm()
    return render(request,"Wallet/card_register.html",{"card":card_form})
def transaction_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render(request,"Wallet/transaction_profile.html",{"transactions":transaction})
def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=CustomerTransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transactionProfile",id=transaction.id)
    else:
        form=CustomerTransactionForm(instance=transaction)
        return render(request,"Wallet/edit_transaction.html",{"forms":form})
             
def list_card(request):
    card=Card.objects.all()
    return render(request,"Wallet/list_card.html",{"cards":card})
def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request,"Wallet/card_profile.html",{"cards":card})

def edit_card(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CustomerCardForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            return redirect("cardProfile",id=card.id)
    else:
        return render(request,"Wallet/edit_card.html",{"forms":form})

def register_thirdparty(request):
    if request.method=="POST":
       thirdparty_form=ThirdPartyForm(request.POST)
       if thirdparty_form.is_valid():
           thirdparty_form.save()
    else:
        thirdparty_form=ThirdPartyForm()
    return render(request,"Wallet/register_thirdp.html",{"third":thirdparty_form})

def list_thirdparty(request):
    thirds=ThirdParty.objects.all()
    return render (request,'Wallet/thirdparty_list.html',{"thirdpartys":thirds})

def register_notification(request):
    if request.method=="POST":
       form_notify=CustomerNotificationForm(request.POST)
       if form_notify.is_valid():
           form_notify.save()
    else:
        form_notify=CustomerNotificationForm()
    return render(request,"Wallet/notification.html",{"notify":form_notify})

def notification_list(request):
    notification=Notification.objects.all()
    return render (request,'Wallet/list_notifications.html',{"notifications":notification})

def register_loan(request):
    if request.method=="POST":
       loan_form=LoanForm(request.POST)
       if loan_form.is_valid():
           loan_form.save()
    else:
           loan_form=LoanForm()
    return render(request,"Wallet/loan.html",{"loan":loan_form} )

def list_loan(request):
    loan=Loan.objects.all()
    return render(request,'Wallet/list_loan.html',{"loans":loan})

def register_reward(request):
    if request.method=="POST":
       reward_form=RewardForm(request.POST)
       if reward_form.is_valid():
           reward_form.save()
    else:
        reward_form=RewardForm()
    return render(request,"Wallet/transaction_reward.html",{"reward":reward_form}
    )

def list_reward(request):
    reward=Reward.objects.all()
    return render(request,"Wallet/list_rewards.html",{"rewards":reward})

def register_receipt(request):
    if request.method=="POST":
       receipt_form=TransactionRecieptForm(request.POST)
       if receipt_form.is_valid():
           receipt_form.save()
       else:
            receipt_form=TransactionRecieptForm()
       return render(request,"Wallet/transaction_reciept.html", {"receipt":receipt_form})

def list_receipts(request):
    reciept=Reciept.objects.all()
    return render(request,"Wallet/list_reciepts.html",{"receipts":reciept})

def receipt_profile(request,id):
     reciept=Reciept.objects.get(id=id)
     return render(request,"Wallet/reciept_profile.html",{"reciepts":reciept})

def edit_receipts(request,id):
     receipt=Reciept.objects.get(id=id)
     if request.method=="POST":
        form=TransactionRecieptForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receiptProfile",id=receipt.id)
     else:
        form=TransactionRecieptForm(instance=receipt)
        return render(request,"Wallet/edit_reciept.html",{"forms":form})
     