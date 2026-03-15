from django.urls import path



from .views import products_list, product_list, product_detail



urlpatterns = [
    path('api/', products_list, name='products_api'),
    path('', product_list, name='product_list'),
    
    path('product/<int:pk>/', product_detail, name='product_detail'),

]



