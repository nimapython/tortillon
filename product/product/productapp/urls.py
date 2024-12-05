from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
  path('detail/<int:product_id>/', views.detail, name='detail'),
      path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('place_order/', views.place_order, name='place_order'),


]
