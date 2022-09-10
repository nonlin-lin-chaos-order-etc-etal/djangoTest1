import time

from django.db import models


# Модели Discount, Tax, которые можно прикрепить к модели Order
# и связать с соответствующими атрибутами при создании платежа
# в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме


class TaxRate(models.Model):
    tax_rate_id = models.CharField(max_length=255, default=None, blank=True, null=True)
    object = models.CharField(max_length=255, default="tax_rate")
    active = models.BooleanField(default=True)
    country = models.CharField(max_length=2, default="US")
    created = models.IntegerField(default=0, null=True)
    description = models.CharField(max_length=255, default=None, blank=True, null=True)
    display_name = models.CharField(max_length=255, default="VAT")
    inclusive = models.BooleanField(default=False)
    jurisdiction = models.CharField(max_length=255, default="US - CA")
    livemode = models.BooleanField(default=False)
    # "metadata": {},
    percentage = models.FloatField(default=7.25)
    state = models.CharField(max_length=255, default=None, blank=True, null=True)
    tax_type = models.CharField(max_length=255, default="vat")


class Coupon(models.Model):
    coupon_id = models.CharField(max_length=255, default=None, blank=True, null=True)
    object = models.CharField(max_length=255, default="coupon")
    percent_off = models.FloatField(default=0.0)
    duration = models.CharField(max_length=255, default=None, blank=True, null=True)
    duration_in_months = models.PositiveIntegerField(blank=True, default=None, null=True)


class PromoCode(models.Model):
    promocode_id = models.CharField(max_length=255, default=None, blank=True, null=True)
    object = models.CharField(max_length=255, default="promotion_code")
    coupon = models.OneToOneField(Coupon, blank=True, null=True, default=None, on_delete=models.CASCADE)


class Order(models.Model):
    pass


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    # Stripe price https://stripe.com/docs/currencies#zero-decimal
    price = models.IntegerField(default=0)

    # Stripe currency code
    currency = models.CharField(default="usd", max_length=15)

    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class FixedTax(models.Model):
    tax_rate = models.ForeignKey(TaxRate, related_name="fixed_tax_rates", on_delete=models.CASCADE, default=None, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="fixed_tax_rates")


class DynamicTax(models.Model):
    tax_rate = models.ForeignKey(TaxRate, related_name="dynamic_tax_rates", on_delete=models.CASCADE, default=None, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="dynamic_tax_rates")


class Discount(models.Model):
    coupon = models.ForeignKey(
        Coupon, on_delete=models.CASCADE, related_name="discounts", blank=True, null=True, default=None)
    promotion_code = models.ForeignKey(
        PromoCode, on_delete=models.CASCADE, related_name="discounts", blank=True, null=True, default=None)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="discounts", blank=True, null=True, default=None)
