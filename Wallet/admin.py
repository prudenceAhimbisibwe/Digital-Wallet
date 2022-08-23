from django.contrib import admin
from .models import Customer
from.models import Reciept 
from.models import ThirdParty
from.models import Wallet
from.models import Account
from.models import Transactions
from.models import Card
from.models import Notification
from.models import Loan
from.models import Reward


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","address","email","phonenumber","age","gender")
    search_fields =("firstname","lastname","address","email","phonenumber","age","gender")

admin.site.register(Customer,CustomerAdmin)  
admin.site.register(Wallet) 
admin.site.register(Account) 
admin.site.register(Transactions) 
admin.site.register(Card) 
admin.site.register(Notification) 
admin.site.register(Loan)  
admin.site.register(Reward)  
admin.site.register(ThirdParty) 
admin.site.register(Reciept) 