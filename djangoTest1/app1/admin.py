from django.contrib import admin

# Register your models here.

from .models import Item, Order, Discount, FixedTax, DynamicTax, TaxRate, Coupon, PromoCode

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(FixedTax)
admin.site.register(DynamicTax)
admin.site.register(TaxRate)
admin.site.register(Coupon)
admin.site.register(PromoCode)
