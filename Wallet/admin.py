from django.contrib import admin
from .models import Account, Card, Customer, Loan, Notification, Reciept, Reward, ThirdParty, Transaction, Wallet


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","address","email","phonenumber","age","gender")
    search_fields =("firstname","lastname","address","email","phonenumber","gender")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ("customer","balance","amount","currency","pin","isactive")
    search_fields =("customer","balance","amount","currency","pin","isactive")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_number","account_name","balance","account_type","wallet")
    search_fields =("account_number","account_name","balance","account_type","wallet")
admin.site.register(Account,AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("wallet","transaction_amount","transaction_charge")
    search_fields =("Wallet","transaction_amount")
admin.site.register(Transaction,TransactionAdmin)
   
class CardAdmin(admin.ModelAdmin):
    list_display = ("card_name","card_type","card_number","security_code","issuer","issued_date")
    search_fields =("card_name","card_type","card_number","security_code","issuer","issued_date")
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ("name","currency","phone_number","id","transaction_cost","location")
    search_fields =("name","currency","phone_number","id","transaction_cost","location")
admin.site.register(ThirdParty,ThirdPartyAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ("amount","issued_date","due_date","amount","loan_term","loan_balance","guarantee","loan_purpose","wallet")
    search_fields =("amount","issued_date","due_date","amount","loan_term","loan_balance","guarantee","loan_purpose","wallet")
admin.site.register(Loan,LoanAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("name","message","date","title","recipient","notification_id","status")
    search_fields =("name","message","date","title","recipient","notification_id","status")
admin.site.register(Notification,NotificationAdmin)


class RecieptAdmin(admin.ModelAdmin):
    list_display = ("name","date","reciept_number","reciept_type","reciept_file")
    search_fields =("name","date","reciept_number","reciept_type","reciept_file")
admin.site.register(Reciept,RecieptAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ("reward_date","transaction","customer_id","bonus")
    search_fields =("reward_date","transaction","customer_id","bonus")
admin.site.register(Reward,RewardAdmin)

   
