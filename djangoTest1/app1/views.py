import json
import time

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings

import stripe

from .models import Item, Order, TaxRate, FixedTax, DynamicTax, Discount, Coupon, PromoCode


stripe.api_key = settings.STRIPE_SECRET_API_KEY


def index_view(request):
    return HttpResponse("Hello, world. You're at the app1 index view.")


def tax_rate_view(request, tax_rate_id):
    tax_rate = get_object_or_404(TaxRate, pk=tax_rate_id)
    context = {
        "tax_rate": tax_rate,
        "stripe_key": settings.STRIPE_PUBLISHABLE_API_KEY,
    }
    return render(request, 'app1/tax_rate.html', context)


def coupon_view(request, coupon_id):
    coupon = get_object_or_404(Coupon, pk=coupon_id)
    context = {
        "coupon": coupon,
        "stripe_key": settings.STRIPE_PUBLISHABLE_API_KEY,
    }
    return render(request, 'app1/coupon.html', context)


def promocode_view(request, promocode_id):
    promocode = get_object_or_404(PromoCode, pk=promocode_id)
    context = {
        "promocode": promocode,
        "stripe_key": settings.STRIPE_PUBLISHABLE_API_KEY,
    }
    return render(request, 'app1/promocode.html', context)


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


def item_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.price_str = "{:0,.2f}{}".format(float(item.price/100.0), item.currency.upper())
    context = {
        "item": item,
        "stripe_key": settings.STRIPE_PUBLISHABLE_API_KEY,
    }
    return render(request, 'app1/item.html', context)


def buy_view(request, order_id):
    print(f"buying order {order_id}")
    order = get_object_or_404(Order, pk=order_id)
    print(f"found order")
    discounts = []
    for discount in order.discounts.all():
        if discount.coupon is not None:
            discounts.append({"coupon":discount.coupon.coupon_id})
        if discount.promotion_code is not None:
            discounts.append({"promotion_code": discount.promotion_code.promocode_id})
    print(f"discounts {discounts}")
    line_items = []
    for item in order.item_set.all():
        fixed_tax_rates = []
        for tax_rate in item.fixed_tax_rates.all():
            fixed_tax_rates.append(tax_rate.tax_rate.tax_rate_id)
        dynamic_tax_rates = []
        for tax_rate in item.dynamic_tax_rates.all():
            dynamic_tax_rates.append(tax_rate.tax_rate.tax_rate_id)
        line_item = {
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    # 'tax_code': item.tax.tax_code,
                },
                'unit_amount': item.price,
                # 'tax_behavior': "inclusive" if item.tax.tax_behavior_inclusive else "exclusive",
            },
            'quantity': 1,
            'tax_rates': fixed_tax_rates,
            'dynamic_tax_rates': dynamic_tax_rates,
        }
        line_items.append(line_item)
    session = stripe.checkout.Session.create(
        line_items=line_items,
        discounts=discounts,
        mode='payment',
        success_url=f'{settings.STRIPE_CALLBACKS_URL_PREFIX}success',
        cancel_url=f'{settings.STRIPE_CALLBACKS_URL_PREFIX}cancel',
      )
    return HttpResponse(json.dumps(session), content_type='application/json')


def create_tax_rate_view(request, tax_rate_id):
    tax = get_object_or_404(TaxRate, pk=tax_rate_id)
    tax_object = stripe.TaxRate.create(
        display_name=tax.display_name,
        description=tax.description,
        jurisdiction=tax.jurisdiction,
        percentage=tax.percentage,
        inclusive=tax.inclusive,
    )
    tax.tax_rate_id = tax_object["id"]
    tax.created = int(tax_object["created"])
    tax.save()
    return HttpResponse(json.dumps({"ok": True}), content_type='application/json')


def create_coupon_view(request, coupon_id):
    coupon = get_object_or_404(Coupon, pk=coupon_id)
    coupon_object = stripe.Coupon.create(
        percent_off=coupon.percent_off,
        duration=coupon.duration,
        duration_in_months=coupon.duration_in_months,
    )
    coupon.coupon_id = coupon_object["id"]
    coupon.created = int(coupon_object["created"])
    coupon.save()
    return HttpResponse(json.dumps({"ok": True}), content_type='application/json')


def create_promocode_view(request, promocode_id):
    promocode = get_object_or_404(PromoCode, pk=promocode_id)
    promocode_object = stripe.PromotionCode.create(
        coupon=promocode.coupon.coupon_id
    )
    promocode.promocode_id = promocode_object["id"]
    promocode.created = int(promocode_object["created"])
    promocode.save()
    return HttpResponse(json.dumps({"ok": True}), content_type='application/json')


def success_view(request):
    return render(request, 'app1/success.html')


def cancel_view(request):
    return render(request, 'app1/cancel.html')
