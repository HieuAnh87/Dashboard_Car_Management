from django.urls import path
from ecommerce import views

urlpatterns = [
    # Car
    path('products', views.ProductsView.as_view(), name='car-products'),
    path('productdetail', views.ProductDetailView.as_view(), name='car-productdetail'),
    path('orders', views.OrdersView.as_view(), name='car-orders'),
    path('customers', views.CustomersView.as_view(), name='car-customers'),
    path('cart', views.CartView.as_view(), name='car-cart'),
    path('checkout', views.CheckOutView.as_view(), name='car-checkout'),
    path('shops', views.ShopsView.as_view(), name='car-shops'),
    path('addproduct', views.AddProductView.as_view(), name='car-addproduct'),
]
