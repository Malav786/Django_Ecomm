from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name='cart_summary'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/', views.cart_delete, name='remove_cart_deletefrom_cart'),
    path('update/', views.cart_update, name='cart_update'),

]