from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    # Stripe price https://stripe.com/docs/currencies#zero-decimal
    price = models.IntegerField(default=0)
