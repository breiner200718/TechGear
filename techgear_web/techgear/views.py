import requests
from django.shortcuts import render


API_URL = "https://techgear-api-qqz2.onrender.com"


def productos(request):
    try:
        respuesta = requests.get(
            f"{API_URL}/productos/",
            timeout=5
        )

        if respuesta.status_code == 200:
            productos = respuesta.json()

            return render(
                request,
                "techgear/productos.html",
                {
                    "productos": productos
                }
            )

        try:
            detalle = respuesta.json().get(
                "detail",
                "No fue posible obtener los productos."
            )
        except ValueError:
            detalle = "No fue posible obtener los productos."

        return render(
            request,
            "techgear/productos.html",
            {
                "productos": [],
                "error": detalle
            }
        )

    except requests.exceptions.ConnectionError:
        return render(
            request,
            "techgear/productos.html",
            {
                "productos": [],
                "error": "No se pudo conectar con la API. Verifica que el servidor esté encendido."
            }
        )

    except requests.exceptions.Timeout:
        return render(
            request,
            "techgear/productos.html",
            {
                "productos": [],
                "error": "La API tardó demasiado en responder. Intenta nuevamente."
            }
        )

    except requests.exceptions.RequestException:
        return render(
            request,
            "techgear/productos.html",
            {
                "productos": [],
                "error": "Ocurrió un error al consultar los productos."
            }
        )


def pedidos(request):
    try:
        respuesta = requests.get(
            f"{API_URL}/pedidos/",
            timeout=5
        )

        if respuesta.status_code == 200:
            pedidos = respuesta.json()

            return render(
                request,
                "techgear/pedidos.html",
                {
                    "pedidos": pedidos
                }
            )

        try:
            detalle = respuesta.json().get(
                "detail",
                "No fue posible obtener los pedidos."
            )
        except ValueError:
            detalle = "No fue posible obtener los pedidos."

        return render(
            request,
            "techgear/pedidos.html",
            {
                "pedidos": [],
                "error": detalle
            }
        )

    except requests.exceptions.ConnectionError:
        return render(
            request,
            "techgear/pedidos.html",
            {
                "pedidos": [],
                "error": "No se pudo conectar con la API. Verifica que el servidor esté encendido."
            }
        )

    except requests.exceptions.Timeout:
        return render(
            request,
            "techgear/pedidos.html",
            {
                "pedidos": [],
                "error": "La API tardó demasiado en responder. Intenta nuevamente."
            }
        )

    except requests.exceptions.RequestException:
        return render(
            request,
            "techgear/pedidos.html",
            {
                "pedidos": [],
                "error": "Ocurrió un error al consultar los pedidos."
            }
        )


def checkout(request):

    if request.method == "POST":

        try:
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

        except (ValueError, TypeError):
            return render(
                request,
                "techgear/checkout.html",
                {
                    "error": "Los datos de cantidad o total no son válidos."
                }
            )

        try:
            respuesta = requests.post(
                f"{API_URL}/pedidos/",
                json=datos,
                timeout=5
            )

            if respuesta.status_code in (200, 201):
                return render(
                    request,
                    "techgear/checkout.html",
                    {
                        "mensaje": "Pedido creado correctamente."
                    }
                )

            try:
                detalle = respuesta.json().get(
                    "detail",
                    "No se pudo crear el pedido."
                )
            except ValueError:
                detalle = "No se pudo crear el pedido."

            return render(
                request,
                "techgear/checkout.html",
                {
                    "error": detalle
                }
            )

        except requests.exceptions.ConnectionError:
            return render(
                request,
                "techgear/checkout.html",
                {
                    "error": "No se pudo conectar con la API. Verifica que el servidor esté encendido."
                }
            )

        except requests.exceptions.Timeout:
            return render(
                request,
                "techgear/checkout.html",
                {
                    "error": "La API tardó demasiado en responder. Intenta nuevamente."
                }
            )

        except requests.exceptions.RequestException:
            return render(
                request,
                "techgear/checkout.html",
                {
                    "error": "Ocurrió un error al comunicarse con la API."
                }
            )

    return render(
        request,
        "techgear/checkout.html"
    )
def crear_producto(request):

    if request.method == "POST":

        try:
            datos = {
                "nombre": request.POST.get("nombre"),
                "descripcion": request.POST.get("descripcion"),
                "precio": float(request.POST.get("precio")),
                "stock": int(request.POST.get("stock")),
                "categoria": request.POST.get("categoria")
            }

        except (ValueError, TypeError):
            return render(
                request,
                "techgear/crear_producto.html",
                {
                    "error": "El precio o el stock no tienen un formato válido."
                }
            )

        try:
            respuesta = requests.post(
                f"{API_URL}/productos/",
                json=datos,
                timeout=5
            )

            if respuesta.status_code in (200, 201):
                return render(
                    request,
                    "techgear/crear_producto.html",
                    {
                        "mensaje": "Producto creado correctamente."
                    }
                )

            try:
                detalle = respuesta.json().get(
                    "detail",
                    "No se pudo crear el producto."
                )
            except ValueError:
                detalle = "No se pudo crear el producto."

            return render(
                request,
                "techgear/crear_producto.html",
                {
                    "error": detalle
                }
            )

        except requests.exceptions.ConnectionError:
            return render(
                request,
                "techgear/crear_producto.html",
                {
                    "error": "No se pudo conectar con la API."
                }
            )

        except requests.exceptions.Timeout:
            return render(
                request,
                "techgear/crear_producto.html",
                {
                    "error": "La API tardó demasiado en responder."
                }
            )

        except requests.exceptions.RequestException:
            return render(
                request,
                "techgear/crear_producto.html",
                {
                    "error": "Ocurrió un error al comunicarse con la API."
                }
            )

    return render(
        request,
        "techgear/crear_producto.html"
    )