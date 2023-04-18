from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views import View

from .models import Products


# Create your views here.

def filter_product_with_category(category):
    products = Products.objects.filter(category=category)
    return products


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
        greeting = {}
        greeting['heading'] = "Cart"
        greeting['pageview'] = "Car Management"
        return render(request, 'car/car-cart.html', greeting)


class CheckOutView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Checkout"
        greeting['pageview'] = "Car Management"
        return render(request, 'car/car-checkout.html', greeting)


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
