from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path(f'buy/<int:item_id>', views.buy_view, name='buy'),
    path(f'item/<int:item_id>', views.item_view, name='item'),
    path(f'success', views.success_view, name='success'),
    path(f'cancel', views.cancel_view, name='cancel'),
]