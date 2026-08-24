import httpx
from django.shortcuts import render


def productos(request):
    respuesta = httpx.get("http://127.0.0.1:8000/productos/")

    productos = []

    if respuesta.status_code == 200:
        productos = respuesta.json()

    return render(
        request,
        "techgear/productos.html",
        {
            "productos": productos
        }
    )

def pedidos(request):
    respuesta = httpx.get("http://127.0.0.1:8000/pedidos/")

    pedidos = []

    if respuesta.status_code == 200:
        pedidos = respuesta.json()

    return render(
        request,
        "techgear/pedidos.html",
        {
            "pedidos": pedidos
        }
    )