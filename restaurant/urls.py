from django.urls import path
from . import views

app_name = "restaurant"

urlpatterns = [
    path('', views.home, name='index'),
    path('menu_item/', views.menu_item, name='menu_item'),
    path('menu_item/<int:pk>/', views.single_menu, name='single_menu'),
    path('menu_item/<int:menu_id>/order/', views.order, name='order'),
    path('reservations/', views.reservations, name='reservations'),
    path('orders', views.order_view, name='order_view'),
]
