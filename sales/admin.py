from django.contrib import admin
from .models import Customer, Bill, Order, Product, Producttype
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_filter=["first_name", "last_name"]
    # list_display=["last_name", "account"]
    
    # mit diesem befehl kann man zum beispiel im
    # account bereich niuchts mehr eingeben
    # readonly_fields = ["account"]
       
    # fieldsets = [
    #     (
    #         None,
    #         {
    #             "fields": ["first_name", "last_name", "email_address", "account"],
    #         },
    #     ),
    #     (
    #         "Advanced options",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ["newsletter_abo"],
    #         },
    #     ),
    # ]


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(Producttype)
admin.site.register(Order)
