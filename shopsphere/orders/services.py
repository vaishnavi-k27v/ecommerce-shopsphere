from django.db import transaction
from product.models import Product
from .models import Order


@transaction.atomic
def create_order(user, product_id, qty):

    product = Product.objects.select_for_update().get(id=product_id)

    if product.stock_quantity < qty:
        raise ValueError("Out of stock")

    product.stock_quantity -= qty
    product.save()

    order = Order.objects.create(
        user=user,
        total_price=product.price * qty
    )

    order.products.add(product)

    return order