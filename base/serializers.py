# from rest_framework import serializers
# from .models import CartItem

# class CartItemSerializer(serializers.ModelSerializer):
#     product_name = serializers.CharField(source="product.name", read_only=True)
#     price = serializers.DecimalField(source="product.price", read_only=True, max_digits=10, decimal_places=2)

#     class Meta:
#         model = CartItem
#         fields = ["id", "product", "product_name", "price", "quantity"]
