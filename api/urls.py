from django.urls import path,include
from rest_framework import routers
from Wallet.models import Card, Customer, Notification, Reciept, Transaction, Wallet,Account,Loan
from .views import AccountBuyAirtimeView, AccountLoanRepaymentView, AccountLoanRequestView, AccountViewSet, AccountWithdrawalView, CardViewSet, CustomerViewSet, ReceiptViewSet, TransactionViewSet, WalletViewSet,LoanViewSet,NotificationViewSet,AccountDepositView,AccountTransferView

router=routers.DefaultRouter()  #fetch resource dynamically
router.register(r'customers',CustomerViewSet,basename=Customer)
router.register(r'wallet',WalletViewSet,basename=Wallet)
router.register(r'accounts',AccountViewSet,basename=Account)
router.register(r'cards',CardViewSet,basename=Card)
router.register(r'transactions',TransactionViewSet,basename=Transaction)
router.register(r'loans',LoanViewSet,basename=Loan)
router.register(r'receipts',ReceiptViewSet,basename=Reciept)
router.register(r'notifications',NotificationViewSet,basename=Notification)

urlpatterns=[
      path("",include(router.urls)),
      path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
      path("deposit/<int:pk>/", AccountDepositView.as_view(), name="deposit-view"),
      path("transfer/<int:pk>/",AccountTransferView.as_view(), name="transfer-view"),
      path("withdrawal/",AccountWithdrawalView.as_view(),name="withrawal-view"),
      path("loan_request/",AccountLoanRequestView.as_view(),name="loan-view"),
      path("loan_repayment/",AccountLoanRepaymentView.as_view(),name="repay-loan-view"),
      path("buy_airtime/",AccountBuyAirtimeView.as_view(),name="repay-loan-view")
]