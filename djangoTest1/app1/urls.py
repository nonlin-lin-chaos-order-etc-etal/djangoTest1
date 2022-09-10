from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path(f'item/<int:item_id>', views.item_view, name='item'),
    path(f'buy/<int:order_id>', views.buy_view, name='buy'),
    path(f'order/<int:order_id>', views.order_view, name='order'),
    path(f'tax_rate/<int:tax_rate_id>', views.tax_rate_view, name='tax_rate'),
    path(f'create-tax-rate/<int:tax_rate_id>', views.create_tax_rate_view, name='create_tax_rate'),
    path(f'coupon/<int:coupon_id>', views.coupon_view, name='coupon'),
    path(f'create-coupon/<int:coupon_id>', views.create_coupon_view, name='create_coupon'),
    path(f'promocode/<int:promocode_id>', views.promocode_view, name='promocode'),
    path(f'create-promocode/<int:promocode_id>', views.create_promocode_view, name='create_promocode'),
    path(f'success', views.success_view, name='success'),
    path(f'cancel', views.cancel_view, name='cancel'),
]

