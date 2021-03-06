from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', views.product, name='product_detail'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/delete<int:product_id>', views.cart_delete, name='cart_delete'),
    path('account/create/', views.sign_up, name='signup'),
    path('account/login/', views.log_in, name='login'),
    path('account/signout/', views.sign_out, name='signout'),
]
