from django.urls import path
from . import views

from .views import create_order, orders_list

urlpatterns = [
    path('create/', create_order),
    path('list/', orders_list),
    path("create-order/", views.create_order),
    path("orders/", views.orders_list),
    path("place-order/<int:product_id>/", views.place_order),
]


