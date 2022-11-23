from django import forms

from .models import Account, Card, Customer, Loan, Notification, Reciept, Reward, ThirdParty, Wallet, Transaction

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        widgets={
             "first_name":forms.TextInput(attrs={ 'class': "form-control"}),
             "last_name": forms.TextInput(attrs={ 'class': "form-control"}),
             "address": forms.TextInput(attrs={ 'class': "form-control"}),
             "email": forms.TextInput(attrs={ 'class': "form-control"}),
             "phone_number": forms.TextInput(attrs={ 'class': "form-control"}),
             "gender": forms.Select(attrs={ 'class': "form-control"}),
             "nationality": forms.TextInput(attrs={ 'class': "form-control"}),
             "age": forms.TextInput(attrs={ 'class': "form-control"}),
             "profile_picture":forms.ClearableFileInput(attrs={ 'class': "form-control"}),
        }

class CustomerWalletForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"
        widgets={
             "customer":forms.Select(attrs={'class':"form-control"}),
             "wallet_id":forms.TextInput(attrs={'class':"form-control"}),
             "currency_supported":forms.NumberInput(attrs={'class':"form-control"}),
        }     

class CustomerAccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"
        widgets={
            "customer":forms.Select(attrs={'class':"form-control"}),
            "balance":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
            "account_number":forms.TextInput(attrs={'class':"form-control"}),
            "account_type":forms.TextInput(attrs={'class':"form-control"}),
            "account_name":forms.TextInput(attrs={'class':"form-control"}),
   }
 
class CustomerTransactionForm(forms.ModelForm):
    class Meta:
        model= Transaction  
        fields="__all__"
        widgets={
            "wallet":forms.Select(attrs={'class':"form-control"}),
            "origin_account":forms.TextInput(attrs={'class':"form-control"}),
            "destination_account":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_ref":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_amount":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_charge":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_date":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_type":forms.TextInput(attrs={'class':"form-control"}),
            
             }   
    
class CustomerCardForm(forms.ModelForm):
    class Meta:
        model= Card 
        fields="__all__"
        widgets={
            "card_number":forms.NumberInput(attrs={'class':"form-control"}),
            "card":forms.Select(attrs={'class':"form-control"}),
            "card_security_code":forms.TextInput(attrs={'class':"form-control"}),
            "issuer":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.Select(attrs={'class':"form-control"}),
            "expiry_date":forms.DateTimeInput(attrs={'class':"form-control"}),

        }

class ThirdPartyForm(forms.ModelForm):
    class Meta:
        model= ThirdParty 
        fields="__all__"
        widgets={
            'account':forms.Select(attrs={'class':"form-control"}),
            "wallet":forms.Select(attrs={'class':"form-control"}),
            "date_of_issue":forms.DateTimeInput(attrs={'class':"form-control"}),
            "amount":forms.NumberInput(attrs={'class':"form-control"})
        }

class CustomerNotificationForm(forms.ModelForm):
    class Meta:
        model= Notification
        fields="__all__"
        widgets={
            "message":forms.Textarea(attrs={'class':"form-control"}),
            "title":forms.TextInput(attrs={'class':"form-control"}),
            "date":forms.DateTimeInput(attrs={'class':"form-control"}),
            "status":forms.Select(attrs={'class':"form-control"}),
            "customer":forms.Select(attrs={'class':"form-control"}),
        }

class TransactionRecieptForm(forms.ModelForm):
    class Meta:
        model= Reciept
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={'class':"form-control"}),
            "date":forms.DateTimeInput(attrs={'class':"form-control"}),
            "reciept_number":forms.NumberInput(attrs={'class':"form-control"}),
            "reciept_type":forms.TextInput(attrs={'class':"form-control"}),
            "receipt_file":forms.ClearableFileInput(attrs={'class':"form-control"}),
            "transaction":forms.NumberInput(attrs={'class':"form-control"}),
            "accout_number":forms.NumberInput(attrs={'class':"form-control"}),
            "total_amount":forms.NumberInput(attrs={'class':"form-control"})
            
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model= Loan
        fields="__all__"
        widgets={
            "amount":forms.NumberInput(attrs={'class':"form-control"}),
            "loan_type":forms.Select(attrs={'class':"form-control"}),
            "loan_term":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.Select(attrs={'class':"form-control"}),
            "guarantee":forms.Select(attrs={'class':"form-control"}),
            "loan_balance":forms.NumberInput(attrs={'class':"form-control"}),
            "issued_date":forms.DateTimeInput(attrs={'class':"form-control"}),
            "due_date":forms.DateTimeInput(attrs={'class':"form-control"}),
        }

class RewardForm(forms.ModelForm):
    class Meta:
        model= Reward
        fields="__all__"
        widgets={
            "date":forms.DateTimeInput(attrs={'class':"form-control"}),
            "recepient":forms.Select(attrs={'class':"form-control"}),
            "bonus":forms.NumberInput(attrs={'class':"form-control"}),
            "customer_id":forms.NumberInput(attrs={'class':"form-control"})
        }
     