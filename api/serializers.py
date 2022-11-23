from dataclasses import field
# from importlib.metadata import MetadataPathFinder
from statistics import mode
from rest_framework import serializers
from Wallet.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fieds="__all__"
        
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fieds="__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fieds="__all__"

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fieds="__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fieds="__all__"

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model= Loan
        fieds="__all__"

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reciept
        fieds="__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fieds="__all__"
