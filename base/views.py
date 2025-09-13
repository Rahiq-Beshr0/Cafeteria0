from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from .serializers import CartItemSerializer
# from .models import CartItem, Product
from .models import Product
@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")  
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


def product_list(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

def cart_view(request):
    cart = request.session.get("cart", {})
    cart = {k: v for k, v in cart.items() if str(k).isdigit()}
    total = sum(float(item["price"]) * item["quantity"] for item in cart.values())
    request.session["cart"] = cart 
    return render(request, "cart.html", {"cart": cart, "total": total})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get("cart", {})
    cart[str(product.id)] = {
        "id": product.id,
        "title": product.title,
        "price": float(product.price),
        "quantity": cart.get(str(product.id), {}).get("quantity", 0) + 1,
        "stock": product.stock,
        "image": product.image.url if product.image else "no image",
    }
    request.session["cart"] = cart
    request.session.modified = True
    return redirect('base:product_list')


def update_quantity(request, product_id, action):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        if action == "inc" and cart[str(product_id)]["quantity"] < cart[str(product_id)]["stock"]:
            cart[str(product_id)]["quantity"] += 1
        elif action == "dec" and cart[str(product_id)]["quantity"] > 1:
            cart[str(product_id)]["quantity"] -= 1
    request.session["cart"] = cart
    return redirect("base:cart_view")


def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session["cart"] = cart
    return redirect("base:cart_view")


def clear_cart(request):
    request.session["cart"] = {}
    return redirect("base:cart_view")


