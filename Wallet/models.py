
from datetime import datetime
from email import message
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
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender_choices=(
        ('F','Female'),
        ('M','Male'),
        ('O','Other')
    )
    gender=models.CharField(max_length=10,choices=gender_choices,null=True)
    nationality=models.CharField(max_length=30, null=True)
    # def __str__(self):
    #     return str(self.firstname)      

class Wallet(models.Model):
    customer=models.OneToOneField(null=True,on_delete=models.CASCADE,to=Customer)
    currency_supported=models.CharField(max_length=27)
    wallet_id=models.IntegerField(null=True)
    
class Account(models.Model):
    account_number=models.IntegerField(default=0, null=True)
    account_name=models.CharField(max_length=15,null=True)
    account_type=models.CharField(max_length=20,null=True)
    pin=models.PositiveSmallIntegerField(null=True)
    balance=models.IntegerField(null=True)
    date_created=models.DateTimeField(default=datetime.now)
    customer=models.ForeignKey(to=Customer, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return str(self.customer)
    
    def deposit(self,amount):
        if amount< 0:
            message="Invalid amount"
            status=403
        else:
            self.balance += amount
            self.save()
            message=f"You have deposited this {amount}, your new balance is {self.balance}"
            status=200
        return message, status
    
    def withdraw(self,amount):
        if amount< 0:
            message="Invalid amount"
            status=403
        else:
            self.balance -= amount
            self.save()
            message=f"Hello {self.customer} you have withdrawn this Ksh.{amount}, your new balance is Ksh.{self.account_balance}"
            status=200
        return message, status
    
    def transfer(self,destination,amount):
        if amount <= 0:
            message =  "Invalid amount"
            status = 403
        elif amount > self.balance:
            message =  "Insufficient balance for your account"
            status = 403
        else:
            self.balance -= amount
            self.save()
            destination.deposit(amount)    #belongs to second account
            message = f"You have transfered {amount}, your new balance is {self.balance}"
            status = 200
        return message, status
    
    # @property
    def loan_request(self,amount):
        self.loan_balance2=0
        if amount <= 0:
            message =  "Invalid amount"
            status = 403
        else:
            self.loan_balance2+= amount
            self.balance += amount
            self.save()
            message = f"Hello {self.customer}, You have requested for loan of  Ksh.{amount}, your new balance is {self.account_balance}"
            status = 200
        return message, status
    
    # @property
    def loan_repayment(self,amount):
        # self.loan_balance2=0
        if amount <= 0:
            message =  "Invalid amount"
            status = 403
        else:
            self.balance -= self.loan_balance2
            self.save()
            message = f"Hello {self.customer}, Your  loan of  Ksh.{self.loan_balance2} has been repayed, your new balance is {self.account_balance} "
            status = 200
        return message, status
    
    def buy_airtime(self,amount):
        if amount< 0:
            message="Invalid amount"
            status=403
        else:
            self.balance -= amount
            self.save()
            message=f" Hello {self.customer}, You have bought airtime for Ksh.{amount}, your new balance is {self.balance} on {self.date_created.strftime('%d/%m/%y/, %H/%M/%S')} "
            status=200
        return message, status
       
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
    # def __str__(self):
    #     return (self.wallet)
    
class Card(models.Model):
    card_number=models.IntegerField()
    expiry_date=models.DateTimeField(default=datetime.now)
    card_type_choices=(
        ('Debit','debit'),
        ('credit','credit')
    )
    card=models.CharField(max_length=6,choices=card_type_choices,null=True)
    card_security_code=models.CharField(max_length=6)
    issuer=models.CharField(max_length=33)
    wallet=models.ForeignKey(on_delete=models.CASCADE,to=Wallet)

class ThirdParty(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="acc",null=True)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name="wall",null=True)
    date_of_issue=models.DateTimeField(default=datetime.now)
    amount=models.BigIntegerField(null=True) 

class Notification(models.Model):
    message=models.CharField(max_length=10000)
    title=models.CharField(max_length=900)
    date=models.DateTimeField(default=datetime.now)
    state=(
        ('active','active'),
        ('passive','passive')
    )
    status=models.CharField(max_length=7,choices=state,null=True)
    customer=models.ForeignKey(on_delete=models.CASCADE,to=Customer)

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
    transaction=models.ForeignKey(on_delete=models.CASCADE, to =Transaction)
    account_number=models.IntegerField()
    total_amount=models.IntegerField()
    # def __str__(self):
    #     return (self.transaction)

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
    recepient=models.ForeignKey(on_delete=models.CASCADE,to=Customer)
    customer_id=models.IntegerField()
    bonus=models.IntegerField(null=True)
    