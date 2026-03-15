# from django.urls import path
# from .views import add_to_cart, cart_items
# from django.urls import path
# from .views import add_to_cart, cart_view


# urlpatterns = [
#     path('add/', add_to_cart),
#     path('items/', cart_items),
# ]

# urlpatterns = [

#     path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
#     path('', cart_view, name='cart_view'),

# ]

from django.urls import path
from .views import (
    api_add_to_cart,
    cart_items,
    add_product_session_cart,
    cart_view,
    add_product_redis_cart
)

urlpatterns = [

    # API endpoints
    path('api/add/', api_add_to_cart, name='api_add_to_cart'),
    path('api/items/', cart_items, name='cart_items'),

    # Session cart
    path('add/<int:product_id>/', add_product_session_cart, name='add_to_cart'),
    path('view/', cart_view, name='cart_view'),

    # Redis cart
    path('redis/add/<int:product_id>/', add_product_redis_cart, name='redis_add_cart'),
]