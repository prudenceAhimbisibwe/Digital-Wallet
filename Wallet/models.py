

from email.policy import default
from django.utils import timezone
from django.db import models


# Create your models here.
class Customer(models.Model):
    firstname= models.CharField(max_length=15,null=True)
    lastname=models.CharField(max_length=15,null=True)
    address=models.TextField()
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10,null=True)
    age=models.CharField(max_length=10,null=True)
    gender_choices=(
        ('F','Female'),
        ('M','Male'),
        ('O','Other')
    )
    gender=models.CharField(max_length=10,choices=gender_choices,null=True)


class Wallet(models.Model):
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer',null=True)
    balance=models.IntegerField()
    amount=models.IntegerField()
    DateTime=models.DateTimeField(default=timezone.now)
    isactive=models.BooleanField()
    currency=models.CharField(max_length=200,null=True)
    pin=models.CharField( max_length=12,null=True)
    
   

class Account(models.Model):
    account_number=models.IntegerField(default=0, null=True)
    account_name=models.CharField(max_length=15,null=True)
    account_type=models.CharField(max_length=20,null=True)
    balance=models.IntegerField(null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet',null=True)

class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=150,null=True)
    wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name   = 'Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_choices= (
       ('withdraw', 'Withdrawal'),
        ('deposit', 'deposit'),
    )
    transaction_type=models.CharField(max_length=10, choices=transaction_choices,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default=timezone.now)
    original_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_original_account')
    destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')

class Card(models.Model):
    card_name=models.CharField(max_length=20,null=True)
    card_type=models.CharField(max_length=20,null=True)
    card_number=models.IntegerField()
    security_code=models.IntegerField(null=True)
    issued_date=models.DateTimeField(default=timezone.now)
    expiry_date=models.DateTimeField(default=timezone.now)
    serial_number=models.IntegerField()
    credit_limit=models.IntegerField()
    signature=models.CharField(max_length=10,null=True)
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
    card_status=models.CharField(max_length=50,null=True)
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Card_wallet')
    issuer=models.CharField(max_length=20,null=True)


class ThirdParty(models.Model):
    name=models.CharField(max_length=20,null=True)
    account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='ThirdParty_account')
    currency=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='ThirdParty_currency')
    phone_number=models.IntegerField()
    # id=models.IntegerField()
    transaction_cost=models.IntegerField()
    location=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='ThirdParty_location')
    

class Notification(models.Model):
    name=models.CharField(max_length=20,null=True)
    message=models.CharField(max_length=100,null=True)
    date=models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Notification_date')
    title=models.CharField(max_length=50,null=True)
    recipient=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Notification_recipient')
    notification_id=models.CharField( max_length=20,null=True)
    status=models.CharField(max_length=100,null=True)

class Reciept(models.Model):
    name=models.CharField(max_length=20,null=True)
    date=models.DateTimeField(default=timezone.now)
    reciept_number=models.IntegerField(null=True)
    reciept_choice=(
        ('D','debt'),
        ('C','credit')
    )
    reciept_type=models.CharField(max_length=10, choices=reciept_choice,null=True)
    reciept_file=models.FileField(upload_to='Wallet/')
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Reciept_transaction')
    account_number=models.IntegerField()
    total_amount=models.IntegerField()

class Loan(models.Model):
    amount=models.IntegerField()
    issued_date=models.DateField()
    due_date=models.DateTimeField(default=timezone.now)
    loan_term=models.CharField(max_length=100,null=True)
    loan_balance=models.IntegerField()
    guarantee=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Loan_guarentee')
    loan_purpose=models.CharField(max_length=100,null=True)
    wallet=models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Loan_wallet')

class Reward(models.Model):
    reward_date=models.DateTimeField(default=timezone.now)
    transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Reward_transaction')
    customer_id=models.IntegerField()
    bonus=models.IntegerField()
    