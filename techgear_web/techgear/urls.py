from django.urls import path
from . import views

urlpatterns = [
    path("productos/", views.productos, name="productos"),
    path("crear-producto/", views.crear_producto, name="crear_producto"),
    path("pedidos/", views.pedidos, name="pedidos"),
    path("checkout/", views.checkout, name="checkout"),
]