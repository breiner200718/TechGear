import requests
from django.shortcuts import render


def productos(request):
    respuesta = requests.get("http://127.0.0.1:8000/productos/")

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
    respuesta = requests.get("http://127.0.0.1:8000/pedidos/")

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

def checkout(request):

    if request.method == "POST":

        datos = {
            "cliente": {
                "nombre": request.POST.get("nombre"),
                "telefono": request.POST.get("telefono"),
                "direccion": request.POST.get("direccion"),
                "ciudad": request.POST.get("ciudad")
            },
            "producto_id": request.POST.get("producto_id"),
            "cantidad": int(request.POST.get("cantidad")),
            "total": float(request.POST.get("total"))
        }

        respuesta = requests.post(
            "http://127.0.0.1:8000/pedidos/",
            json=datos
        )

        if respuesta.status_code == 200:
            return render(
                request,
                "techgear/checkout.html",
                {
                    "mensaje": "Pedido creado correctamente"
                }
            )

        return render(
            request,
            "techgear/checkout.html",
            {
                "error": "No se pudo crear el pedido"
            }
        )

    return render(request, "techgear/checkout.html")