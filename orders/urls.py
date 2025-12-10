from django.urls import path
from .views import CartListCreateView, CartItemDetailView, OrderCreateView, OrderListView

urlpatterns = [
    #cart urls
    path('cart/', CartListCreateView.as_view(), name='cart_list_create'),
    path('cart/<int:pk>/', CartItemDetailView.as_view(), name='cart_item_detail'),

    #order urls
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
]
