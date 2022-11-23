from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.generic.base import View
# from rest_framework.views import APIView
from Wallet import views
from email import message
from urllib import response
from django.shortcuts import render
from Wallet.models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()  #request info
    serializer_class=CustomerSerializer   #type of Serializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):  #class based view working with crud operations 
    queryset=Account.objects.all().order_by("customer")
    serializer_class=AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset=Loan.objects.all()
    serializer_class=LoanSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset=Reciept.objects.all()
    serializer_class=ReceiptSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer

class AccountDepositView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]    #creating account id 
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.deposit(amount) 
        return Response (message,status=status)

    def get(self,request,pk,format=None):
        account = Account.objects.get(pk=pk)   #create for single object view
        if request.method == 'GET':             #specified request to be get method 
            serializer =AccountSerializer(account)   #serialize the object
            return Response(serializer.data)  

class AccountWithdrawalView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]    #creating account id 
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.withdraw(amount) 
        return Response (message,status=status)
    
#create an Api for a single account.
        
class AccountTransferView(views.APIView):
    def post(self,request,pk,format=None):
        account_1=Account.objects.get(pk=pk)
        account_id=request.data["destination"]   
        amount=request.data["amount"]  #to handle json data coming
        # destination_account=request.data["destination"]
        
        try:
            account=Account.objects.get(id=account_id)    #get destination account
        except ObjectDoesNotExist:  #when no object exist
            return Response("Account Not Found", status=404)
        message, status = account_1.transfer(account,amount)    #transfer to destination
        return Response (message,status=status)
    
class AccountLoanRequestView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.loan_request(amount) 
        return Response (message,status=status)

class AccountLoanRepaymentView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        amount=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)    
        except ObjectDoesNotExist:  #whenn no object exist
            return Response("Account Not Found", status=404)
        message, status = account.loan_repayment(amount) 
        return Response (message,status=status)
    
class AccountBuyAirtimeView(views.APIView):
    def post(self,request,format=None):
        account_id=request.data["account_id"]
        airtime_money=request.data["amount"]
        try:
            account=Account.objects.get(id=account_id)
        except ObjectDoesNotExist:
            return Response("Account not found",status=404)
        message,status=account.buy_airtime(airtime_money)
        return Response(message,status=status)       
