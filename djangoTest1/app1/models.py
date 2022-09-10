from django.db import models


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
