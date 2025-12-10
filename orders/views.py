from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CartItem, Order, OrderItem
from .serializers import CartItemSerializer, OrderSerializer
from products.models import Product
from django.db.models import F, Sum


"""cart API"""
class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return CartItem.objects.none()  # this returns empty queryset for swagger
        return CartItem.objects.filter(user=self.request.user)


"""order API"""
class OrderCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"detail": "Cart is empty"}, status=400)

        order = Order.objects.create(user=request.user)
        total = 0

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            total += item.product.price * item.quantity

        order.total_price = total
        order.save()
        """emptying the cart after placing order"""
        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
