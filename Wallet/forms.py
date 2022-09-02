from django import forms

from .models import Account, Card, Customer, Loan, Notification, Reciept, Reward, ThirdParty, Wallet, Transaction

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class CustomerWalletForm(forms.ModelForm):
    class Meta:
        model=Wallet
        fields="__all__"

class CustomerAccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"

class CustomerTransactionForm(forms.ModelForm):
    class Meta:
        model= Transaction  
        fields="__all__"

class CustomerCardForm(forms.ModelForm):
    class Meta:
        model= Card 
        fields="__all__"

class ThirdPartyForm(forms.ModelForm):
    class Meta:
        model= ThirdParty 
        fields="__all__"

class CustomerNotificationForm(forms.ModelForm):
    class Meta:
        model= Notification
        fields="__all__"

class TransactionRecieptForm(forms.ModelForm):
    class Meta:
        model= Reciept
        fields="__all__"

class LoanForm(forms.ModelForm):
    class Meta:
        model= Loan
        fields="__all__"

class RewardForm(forms.ModelForm):
    class Meta:
        model= Reward
        fields="__all__"