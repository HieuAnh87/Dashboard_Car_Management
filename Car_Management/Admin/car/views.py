from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import View

from .models import Products, CartOrder, CartOrderItems


# Add to cart
def add_to_cart(request):
    if request.method == 'POST':
        prod_id = request.POST.get('prod_id')
        product_check = Products.objects.get(pid=prod_id)
        # print(product_check)
        product_id_default = product_check.id
        # print(product_id_default)
        if product_check:
            if (CartOrder.objects.filter(user=request.user.id, product=product_id_default)):
                return JsonResponse({'success': False, 'message': 'Product already in cart'})
            else:
                # Cart.objects.create(user=request.user, product=prod_id, quantity=1)
                cart_item = CartOrder(user=request.user, product=product_check, quantity=1)
                cart_item.save()
                return JsonResponse({'success': True, 'message': 'Product added to cart'})
        else:
            return JsonResponse({'success': False})


def update_cart_item(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        try:
            cart_item = CartOrder.objects.get(cid=id)
            product = cart_item.product
            stock_count = product.stock_count
            if stock_count is not None and int(quantity) > int(stock_count):
                return JsonResponse({'error': 'Not enough stock.'})
            cart_item.quantity = quantity
            cart_item.save()
            total_price = cart_item.get_price()
            subtotal = sum(item.get_price() for item in CartOrder.objects.filter(user=request.user.id))
            tax_rate = Decimal('0.05')  # 5% tax rate
            discount = 0  # example discount value
            tax = subtotal * tax_rate
            total = subtotal + tax - discount

            try:
                cart_order_item = CartOrderItems.objects.get(user=request.user.id)
                cart_order_item.grand_total = subtotal
                cart_order_item.tax = tax
                cart_order_item.total_price = total
                cart_order_item.save()
            except CartOrderItems.DoesNotExist:
                # ValueError: Cannot assign "1": "CartOrderItems.user" must be a "User" instance.
                CartOrderItems.objects.create(user=request.user, grand_total=subtotal, tax=tax, total_price=total,
                                              cart_order=cart_item)
            return JsonResponse({'success': 'Cart item updated.',
                                 'total_price': total_price,
                                 'subtotal': str(subtotal),
                                 'discount': str(discount),
                                 'tax': str(tax),
                                 'total': str(total)})
        except CartOrder.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})


class DeleteCartItemView(LoginRequiredMixin, View):
    def post(self, request):
        cid = request.POST.get('cid')
        cart_item = get_object_or_404(CartOrder, cid=cid, user=request.user)
        print(cart_item)
        cart_item.delete()
        return redirect('car-cart')


# class CheckOutCartItemView(LoginRequiredMixin, View):
#     def get(self, request):
#         cart_order_item = CartOrderItems.objects.get(user=request.user.id)
#         context = {
#             'heading': "Checkout",
#             'pageview': "Car Management",
#             'cart_order_item': cart_order_item
#         }
#         return render(request, 'car/car-checkout.html', context)



class ProductsView(LoginRequiredMixin, View):
    def get(self, request):
        # Get all products ordered by title
        products = Products.objects.order_by('-title')
        # Get the category from the request's GET parameters
        category = request.GET.get('category')
        if category:
            products = products.filter(category=category)  # Filter products by category if category is provided
        search_query = request.GET.get('search')
        # SEARCH by title
        if search_query:
            products = products.filter(
                title__icontains=search_query)  # Filter products by title if search query is provided
        # Create a Paginator object with 6 items per page
        paginator = Paginator(products, 6)
        # Get the current page number from the request's GET parameters
        page_number = request.GET.get('page')
        # Get the Page object for the current page
        try:
            paginated_products = paginator.page(page_number)
        except PageNotAnInteger:
            paginated_products = paginator.page(1)
        context = {
            'products': paginated_products,
            'heading': "Products",
            'pageview': "Car Management"}

        return render(request, 'car/car-products.html', context)


class ProductDetailView(LoginRequiredMixin, View):
    def get(self, request, pid):
        product = Products.objects.get(pid=pid)
        # products = Products.objects.filter(category=product.category).exclude(pid=pid)
        greeting = {}
        greeting['heading'] = "Product Detail"
        greeting['pageview'] = "Car Management"
        greeting['product'] = product
        return render(request, 'car/car-productdetail.html', greeting)


class OrdersView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Orders"
        greeting['pageview'] = "Car Management"
        return render(request, 'car/car-orders.html', greeting)


#
#
# class CustomersView(LoginRequiredMixin, View):
#     def get(self, request):
#         form = CustomersForm()
#         customers_record = Customer.objects.all()
#         p = Paginator(customers_record, 8)
#         page = request.GET.get('page')
#         if p == None:
#             page = int(1)
#         page_obj = p.get_page(page)
#         greeting = {}
#         greeting['heading'] = "Customers"
#         greeting['pageview'] = "Ecommerce"
#         greeting['page_obj'] = page_obj
#         greeting['form'] = form
#         greeting['form1'] = EditCustomersForm()
#         return render(request, 'car/car-customers.html', greeting)
#
#     def post(self, request):
#         if request.method == "POST":
#             if "addcustomer" in request.POST:
#                 form = CustomersForm(request.POST)
#                 form.save()
#                 page_number = request.POST['page_number']
#                 return redirect("/car/customers" + "?page=" + str(page_number))
#             if "editcustomer" in request.POST:
#                 id = request.POST['id']
#                 username = request.POST['username']
#                 email = request.POST['email']
#                 phone = request.POST['phone']
#                 rating = request.POST['rating']
#                 wallet_balance = request.POST['wallet_balance']
#                 address = request.POST['address']
#                 page_number = request.POST['page_number']
#
#                 user = Customers.objects.filter(id=id).update(username=username, email=email, phone=phone,
#                                                               rating=rating, wallet_balance=wallet_balance,
#                                                               address=address)
#                 return redirect("/car/customers" + "?page=" + str(page_number))
#             if "deleteCustomer" in request.POST:
#                 id = request.POST['id']
#                 obj = Customers.objects.filter(id=id).first()
#                 obj.delete()
#                 return HttpResponse()
#
#
# Edit Customer
class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart_items = CartOrder.objects.filter(user=request.user.id)
        subtotal = sum(item.get_price() for item in cart_items)
        tax_rate = Decimal('0.05')  # 5% tax rate
        discount = 0  # example discount value
        tax = subtotal * tax_rate
        total = subtotal + tax - discount
        context = {
            'heading': "Cart",
            'pageview': "Car Management",
            'cart_items': cart_items,
            'subtotal': subtotal,
            'tax': tax,
            'discount': discount,
            'total': total,
        }
        return render(request, 'car/car-cart.html', context)

    # def post(self, request):
    #     if request.method == "POST":
    #         if "deleteCartItem" in request.POST:
    #             id = request.POST['id']
    #             obj = CartOrder.objects.filter(id=id).first()
    #             obj.delete()
    #             return HttpResponse()


class CheckOutView(LoginRequiredMixin, View):
    def get(self, request):
        cart_order_item = CartOrderItems.objects.get(user=request.user.id)
        cart_item = CartOrder.objects.filter(user=request.user.id)
        # print(cart_order_item.cart_order.all())
        context = {
            'heading': "Checkout",
            'pageview': "Car Management",
            'cart_order_item': cart_order_item,
            'cart_item': cart_item,
            'subtotal': cart_order_item.grand_total,
            'tax': cart_order_item.tax,
            'total': cart_order_item.total_price,
        }
        return render(request, 'car/car-checkout.html', context)

    def post(self, request):
        name = request.POST.get('billing-name')
        email = request.POST.get('billing-email-address')
        phone = request.POST.get('billing-phone')
        address = request.POST.get('billing-address')
        city = request.POST.get('city')
        disrict = request.POST.get('disrict')
        ward = request.POST.get('ward')

        print(name, email, phone, address, city, disrict, ward)

        return redirect('/car/checkout')




class ShopsView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Shops"
        greeting['pageview'] = "Car Management"
        return render(request, 'car/car-shops.html', greeting)


class AddProductView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Add Product"
        greeting['pageview'] = "Car Management"
        return render(request, 'car/car-addproduct.html', greeting)
