# shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('product/add/', views.product_create, name='product_create'),
 path('product/<int:product_id>/edit/', views.product_update, name='product_update'),
 path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
]
