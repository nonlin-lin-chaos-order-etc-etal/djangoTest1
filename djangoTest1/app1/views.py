import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings

import stripe

from .models import Item, Order


stripe.api_key = settings.STRIPE_SECRET_API_KEY


def index_view(request):
    return HttpResponse("Hello, world. You're at the app1 index view.")


def order_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = []
    for item in order.item_set.all():
        item.price_str = "{:0,.2f}{}".format(float(item.price/100.0), item.currency.upper())
        items.append(item)
    context = {
        "order": order,
        "items": items,
        "stripe_key": settings.STRIPE_PUBLISHABLE_API_KEY,
    }
    return render(request, 'app1/order.html', context)


def buy_view(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    line_items = []
    for item in order.item_set.all():
        line_item = {
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }
        line_items.append(line_item)
    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url=f'{settings.STRIPE_CALLBACKS_URL_PREFIX}success',
        cancel_url=f'{settings.STRIPE_CALLBACKS_URL_PREFIX}cancel',
      )
    return HttpResponse(json.dumps(session), content_type='application/json')


def success_view(request):
    return render(request, 'app1/success.html')


def cancel_view(request):
    return render(request, 'app1/cancel.html')
