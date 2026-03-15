
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Order, OrderItem
# from cart.models import CartItem
# from django.http import JsonResponse
# from .services import create_order


# @api_view(['POST'])
# def create_order(request):

#     user = request.user
#     cart_items = CartItem.objects.filter(user=user)

#     total = 0

#     for item in cart_items:
#         total += item.product.price * item.quantity

#     order = Order.objects.create(
#         user=user,
#         total=total
#     )

#     for item in cart_items:
#         OrderItem.objects.create(
#             order=order,
#             product=item.product,
#             quantity=item.quantity,
#             price=item.product.price
#         )

#     cart_items.delete()

#     return Response({"message": "Order placed", "order_id": order.id})


# @api_view(['GET'])
# def orders_list(request):

#     user = request.user
#     orders = Order.objects.filter(user=user)

#     data = []

#     for order in orders:
#         data.append({
#             "order_id": order.id,
#             "total": order.total,
#             "date": order.created_at
#         })

#     return Response(data)

# def place_order(request, product_id):

#     qty = int(request.GET.get("qty", 1))

#     try:
#         order = create_order(request.user, product_id, qty)

#         return JsonResponse({
#             "message": "Order created",
#             "order_id": order.id
#         })

#     except ValueError as e:
#         return JsonResponse({
#             "error": str(e)
#         })

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Order, OrderItem
from cart.models import CartItem


@api_view(['POST'])
def create_order(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    if not cart_items.exists():
        return Response({"error": "Cart is empty"})

    total = 0

    for item in cart_items:
        total += item.product.price * item.quantity

    order = Order.objects.create(
        user=user,
        total=total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return Response({
        "message": "Order placed successfully",
        "order_id": order.id
    })


@api_view(['GET'])
def orders_list(request):
    user = request.user
    orders = Order.objects.filter(user=user)

    data = []

    for order in orders:
        data.append({
            "order_id": order.id,
            "total": order.total,
            "date": order.created_at
        })

    return Response(data)


def place_order(request, product_id):
    qty = int(request.GET.get("qty", 1))

    order = Order.objects.create(
        user=request.user,
        total=0
    )

    OrderItem.objects.create(
        order=order,
        product_id=product_id,
        quantity=qty,
        price=0
    )

    return JsonResponse({
        "message": "Order created",
        "order_id": order.id
    })