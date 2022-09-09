import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings

import stripe

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_API_KEY


def index_view(request):
    return HttpResponse("Hello, world. You're at the app1 index view.")


def item_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.price_str = "{:0,.2f}".format(float(item.price/100.0))
    context = {
        "item": item,
        "stripe_key": settings.STRIPE_PUBLISHABLE_API_KEY,
    }
    return render(request, 'app1/item.html', context)


def buy_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'{settings.STRIPE_CALLBACKS_URL_PREFIX}success',
        cancel_url=f'{settings.STRIPE_CALLBACKS_URL_PREFIX}cancel',
      )
    return HttpResponse(json.dumps(session), content_type='application/json')


def success_view(request):
    return render(request, 'app1/success.html')


def cancel_view(request):
    return render(request, 'app1/cancel.html')
