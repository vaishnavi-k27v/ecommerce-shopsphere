# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import CartItem
# from product.models import Product
# from django.shortcuts import redirect, render
# from .cart import Cart
# from django.http import JsonResponse
# from .redis_cart import add_to_cart



# @api_view(['POST'])
# def add_to_cart(request):

#     user = request.user
#     product_id = request.data.get('product')
#     quantity = request.data.get('quantity')

#     product = Product.objects.get(id=product_id)

#     CartItem.objects.create(
#         user=user,
#         product=product,
#         quantity=quantity
#     )

#     return Response({"message": "Product added to cart"})


# @api_view(['GET'])
# def cart_items(request):

#     user = request.user
#     items = CartItem.objects.filter(user=user)

#     data = []

#     for item in items:
#         data.append({
#             "product": item.product.name,
#             "price": item.product.price,
#             "quantity": item.quantity
#         })

#     return Response(data)

# def add_to_cart(request, product_id):

#     cart = Cart(request)
#     cart.add(product_id)

#     return redirect('cart_view')


# def cart_view(request):

#     cart = Cart(request)
#     items = cart.get_items()

#     return render(request, "cart/cart.html", {"items": items})

# def add_product_to_cart(request, product_id):

#     user_id = request.user.id

#     add_to_cart(user_id, product_id)

#     return JsonResponse({"message": "Product added to cart"})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect, render
from django.http import JsonResponse

from .models import CartItem
from product.models import Product
from .cart import Cart
from .redis_cart import add_to_cart as redis_add_to_cart


# -----------------------------
# API: Add product to cart
# -----------------------------
@api_view(['POST'])
def api_add_to_cart(request):

    user = request.user
    product_id = request.data.get('product')
    quantity = request.data.get('quantity')

    product = Product.objects.get(id=product_id)

    CartItem.objects.create(
        user=user,
        product=product,
        quantity=quantity
    )

    return Response({"message": "Product added to cart"})


# -----------------------------
# API: View cart items
# -----------------------------
@api_view(['GET'])
def cart_items(request):

    user = request.user
    items = CartItem.objects.filter(user=user)

    data = []

    for item in items:
        data.append({
            "product": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity
        })

    return Response(data)


# -----------------------------
# Session Cart (Django)
# -----------------------------
def add_product_session_cart(request, product_id):

    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')


def cart_view(request):

    cart = Cart(request)
    items = cart.get_items()

    return render(request, "cart/cart.html", {"items": items})


# -----------------------------
# Redis Cart
# -----------------------------
def add_product_redis_cart(request, product_id):

    user_id = request.user.id

    redis_add_to_cart(user_id, product_id)

    return JsonResponse({"message": "Product added to Redis cart"})
def add_to_cart(request, product_id):

    cart = Cart(request)
    cart.add(product_id)

    return redirect("cart_view")


def cart_view(request):

    cart = Cart(request)

    items = cart.get_items()

    return render(request, "cart/cart.html", {"items": items})
