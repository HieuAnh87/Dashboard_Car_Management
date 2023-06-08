from datetime import datetime

from allauth.account.views import PasswordSetView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from car.models import Products, Order, Customer

from car.models import StatisticsProducts


# utillity
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Dashboard"
        greeting['pageview'] = "Dashboards"
        return render(request, 'dashboard/dashboard.html', greeting)


def calculate_earnings_for_month(month):
    earnings = (
        Order.objects
        .filter(date_created__month=month)
        .aggregate(total_earnings=Sum('total_price'))
    )
    return earnings['total_earnings'] if earnings['total_earnings'] else 0


class SaasView(LoginRequiredMixin, View):
    def get(self, request):
        product = Products.objects.all()
        order = Order.objects.all()
        customer = Customer.objects.all()
        total = 0
        # get month only
        this_month = datetime.now().month
        # get earning for this month
        earnings_this_month = calculate_earnings_for_month(this_month)
        # get earning for last month
        earnings_last_month = calculate_earnings_for_month(this_month - 1)
        # get percentage change
        percentage_change = ((earnings_this_month - earnings_last_month) / earnings_last_month) * 100
        percentage_change = float("{:.2f}".format(percentage_change))

        for order_ in order:
            total += order_.total_price

        earnings_per_month = Order.objects.filter(date_created__year=2023). \
            annotate(month=TruncMonth('date_created')). \
            values('month').annotate(total_earnings=Sum('total_price')) \
            .order_by('month')
        # print(earnings_per_month)
        for entry in earnings_per_month:
            month = entry['month'].strftime('%B')
            earnings = entry['total_earnings']
            print(f"{month}: ${earnings}")

        earn_per_month = [entry['total_earnings'] for entry in earnings_per_month]
        month = [entry['month'].strftime('%B') for entry in earnings_per_month]

        car_accessories = Products.objects.filter(category='car accessories').count()
        car_accessories = int(car_accessories)

        car_care = Products.objects.filter(category='car care services').count()
        car_care = int(car_care)

        car_exterior = Products.objects.filter(category='car exterior').count()
        car_exterior = int(car_exterior)

        car_interior = Products.objects.filter(category='car interior').count()
        car_interior = int(car_interior)

        car_parts = Products.objects.filter(category='car parts').count()
        car_parts = int(car_parts)

        products_list = ['car accessories', 'car care services', 'car exterior', 'car interior', 'car parts']
        products_number = [car_accessories, car_care, car_exterior, car_interior, car_parts]

        statistic = StatisticsProducts.objects.all().order_by('-total_revenue')[:1]

        for prod in statistic:
            product_name = prod.product.title
            quantity_sold = prod.quantity_sold
            total_rev = prod.total_revenue

        total_revs = StatisticsProducts.objects.aggregate(Sum('quantity_sold'))
        total_value = total_revs['quantity_sold__sum']
        # print(quantity_sold)
        # print(product_name)
        # print(total_revenue)
        print(total_value)

        percent_selling = (quantity_sold / total_value) * 100
        percent_selling = float("{:.2f}".format(percent_selling))


        selling_label = [product_name, 'Total']
        selling_quantity = [quantity_sold, total_value]

        context = {
            'heading': "Car Management",
            'pageview': "Dashboards",
            'product': product,
            'order': order,
            'customer': customer,
            'total': total,
            'products_list': products_list,
            'products_number': products_number,
            'earn_per_month': earn_per_month,
            'month': month,
            'earnings_this_month': earnings_this_month,
            'earnings_last_month': earnings_last_month,
            'percentage_change': percentage_change,
            'total_rev': total_rev,
            'product_name': product_name,
            'selling_label': selling_label,
            'selling_quantity': selling_quantity,
            'percent_selling': percent_selling,
        }
        return render(request, 'dashboard/dashboard-saas.html', context)


# class CryptoView(LoginRequiredMixin, View):
#     def get(self, request):
#         greeting = {}
#         greeting['heading'] = "Crypto"
#         greeting['pageview'] = "Dashboards"
#         return render(request, 'dashboard/dashboard-crypto.html', greeting)
#
#
# class BlogView(LoginRequiredMixin, View):
#     def get(self, request):
#         greeting = {}
#         greeting['heading'] = "Blog"
#         greeting['pageview'] = "Dashboards"
#         return render(request, 'dashboard/dashboard-blog.html', greeting)


class CalendarView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "TUI Calendar"
        greeting['pageview'] = "Calendars"
        return render(request, 'calendar.html', greeting)


class CalendarFullView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Full Calendar"
        greeting['pageview'] = "Calendars"
        return render(request, 'calendar-full.html', greeting)


# class ChatView(LoginRequiredMixin, View):
#     def get(self, request):
#         greeting = {}
#         greeting['heading'] = "Chat"
#         greeting['pageview'] = "Apps"
#         return render(request, 'chat-view.html', greeting)


class FileManagerView(LoginRequiredMixin, View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "File Manager"
        greeting['pageview'] = "Apps"
        return render(request, 'filemanager.html', greeting)


# Authentication
class PagesLoginView(View):
    def get(self, request):
        return render(request, 'authentication/pages-login.html')


class PagesRegisterView(View):
    def get(self, request):
        return render(request, 'authentication/pages-register.html')


class PagesRecoverpwView(View):
    def get(self, request):
        return render(request, 'authentication/pages-recoverpw.html')


class PagesLockscreenView(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen.html')


class PagesConfirmmailView(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail.html')


class PagesEmailVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail.html')


class PagesTwoStepVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail.html')


class PagesLogin2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-login-2.html')


class PagesRegister2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-register-2.html')


class PagesRecoverpw2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-recoverpw2.html')


class PagesLockscreen2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen2.html')


class PagesConfirmmail2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail-2.html')


class PagesEmailVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail-2.html')


class PagesTwoStepVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail-2.html')


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('dashboard')


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy('dashboard')
