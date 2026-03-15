# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.shortcuts import render, get_object_or_404

# from .models import Product


# # -------------------------------
# # API: Get all products
# # -------------------------------
# @api_view(['GET'])
# def product_list(request):

#     product = Product.objects.all()

#     data = []

#     for p in product:
#         data.append({
#             "id": p.id,
#             "name": p.name,
#             "price": p.price,
#             "stock": p.stock_quantity,
#             "description": p.description
#         })

#     return Response(data)


# # -------------------------------
# # Web Page: Product List
# # -------------------------------
# def product_list(request):

#     product = Product.objects.all()

#     return render(
#         request,
#         "product/product_list.html",
#         {"product": product}
#     )


# # -------------------------------
# # Web Page: Product Details
# # -------------------------------
# def product_detail(request, pk):

#     product = get_object_or_404(Product, id=pk)

#     return render(
#         request,
#         "product/product_detail.html",
#         {"product": product}
#     )
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from .models import Product


# -------------------------------
# API: Get all products
# -------------------------------
@api_view(['GET'])
def products_list(request):

    products = Product.objects.all()

    data = []

    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock_quantity,
            "description": p.description
        })

    return Response(data)


# -------------------------------
# Web Page: Product List
# -------------------------------
def product_list(request):

    products = Product.objects.all()

    return render(
        request,
        "products/product_list.html",
        {"products": products}
    )


# -------------------------------
# Web Page: Product Details
# -------------------------------
def product_detail(request, pk):

    product = get_object_or_404(Product, id=pk)

    return render(
        request,
        "products/product_detail.html",
        {"product": product}
    )