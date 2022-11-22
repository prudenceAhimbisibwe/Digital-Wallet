from dataclasses import field
from importlib.metadata import MetadataPathFinder
from statistics import mode
from rest_framework import serializers
from wallet.models import Card, Customer, Receipt, Transaction, Wallet,Account,Loan,Notifcation

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","last_name","age","email","address")
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields=("customer","currency_supported","wallet_id")
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=("account_number","customer","account_balance","pin","loan_balance")
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields=("card_number","expiry_date","card","card_security_code","issuer","walletb")
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=("walletb","origin_account","destination_account","transaction_code","transaction_charge","transaction_amount","transaction_date")
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fields=("loan_amount","loan_type","interest_rate","date")
        # "loan_term","loan_Id","walletb")
class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receipt
        fields=("receipt_date","receipt_number","receipt_file","transaction")
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notifcation
        fieds="__all__"