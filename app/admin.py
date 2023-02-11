from django.contrib import admin

# Register your models here.
from .models import Customer , Plan , Payment ,Operator , Recharge
## customer serializer


# admin.site.register(Customer)
admin.site.register(Plan)
admin.site.register(Payment)
admin.site.register(Operator)
admin.site.register(Recharge)


@admin.register(Customer)
class adminCustomer(admin.ModelAdmin):
    class Meta:
        model=Customer
        list_display=['user','operator', 'Plan','address','Phone']


