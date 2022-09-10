from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path(f'item/<int:item_id>', views.item_view, name='item'),
    path(f'buy/<int:order_id>', views.buy_view, name='buy'),
    path(f'order/<int:order_id>', views.order_view, name='order'),
    path(f'success', views.success_view, name='success'),
    path(f'cancel', views.cancel_view, name='cancel'),
]