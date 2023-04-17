from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


# Create your views here.

class ProductsView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Products"
        greeting['pageview'] = "Car Management"
        return render(request, 'car/car-products.html', greeting)


class ProductDetailView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Product Detail"
        greeting['pageview'] = "Car Management"
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
