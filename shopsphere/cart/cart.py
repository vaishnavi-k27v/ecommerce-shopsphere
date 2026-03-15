# from product.models import Product


# class Cart:

#     def __init__(self, request):

#         self.session = request.session
#         cart = self.session.get('cart')

#         if not cart:
#             cart = self.session['cart'] = {}

#         self.cart = cart


#     def add(self, product_id, quantity=1):

#         if str(product_id) not in self.cart:
#             self.cart[str(product_id)] = quantity
#         else:
#             self.cart[str(product_id)] += quantity

#         self.save()


#     def remove(self, product_id):

#         if str(product_id) in self.cart:
#             del self.cart[str(product_id)]
#             self.save()


#     def save(self):
#         self.session.modified = True


#     def get_items(self):

#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in=product_ids)

#         items = []

#         for product in products:
#             items.append({
#                 "product": product,
#                 "quantity": self.cart[str(product.id)]
#             })

#         return items

from product.models import Product

class Cart:

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart


    def add(self, product_id):

        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = 1
        else:
            self.cart[product_id] += 1

        self.session.modified = True


    def get_items(self):

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        items = []

        for product in products:

            items.append({
                "product": product,
                "quantity": self.cart[str(product.id)]
            })

        return items