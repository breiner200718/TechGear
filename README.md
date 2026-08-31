TechGear
Descripción

TechGear es una aplicación web para la gestión de productos y pedidos de una tienda de hardware y accesorios tecnológicos.

El proyecto está dividido en dos partes principales:

Backend: API desarrollada con FastAPI, encargada de los endpoints, validaciones y conexión con la base de datos.
Frontend: aplicación desarrollada con Django, encargada de las vistas, plantillas HTML y presentación de la información al usuario.

La aplicación utiliza MongoDB como base de datos para el backend y SQLite para la aplicación Django.

Estructura del proyecto
TechGear/
│
├── .venv/                         # Entorno virtual de Python
│   ├── Include/
│   ├── Lib/
│   └── Scripts/
│
├── backend/                       # API Backend - FastAPI
│   │
│   ├── routes/                    # Endpoints de la API
│   │   ├── __init__.py
│   │   ├── pedidos.py             # Endpoints relacionados con pedidos
│   │   └── productos.py           # Endpoints relacionados con productos
│   │
│   ├── schemas/                   # Esquemas de validación con Pydantic
│   │   ├── pedido_schema.py       # Modelo de datos para pedidos
│   │   └── producto_schema.py     # Modelo de datos para productos
│   │
│   ├── .env                       # Variables de entorno
│   ├── database.py                # Conexión con la base de datos
│   └── main.py                    # Punto de entrada de la API FastAPI
│
├── frontend/                      # Aplicación web - Django
│   │
│   ├── config/                    # Configuración principal de Django
│   │   ├── __init__.py
│   │   ├── asgi.py                # Configuración para servidores ASGI
│   │   ├── settings.py            # Configuración del proyecto
│   │   ├── urls.py                # Rutas principales de Django
│   │   └── wsgi.py                # Configuración para servidores WSGI
│   │
│   ├── techgear/                 # Aplicación principal de Django
│   │   ├── migrations/            # Migraciones de la base de datos
│   │   │   └── __init__.py
│   │   │
│   │   ├── templates/
│   │   │   └── techgear/
│   │   │       ├── checkout.html  # Página de checkout
│   │   │       ├── pedidos.html   # Página de pedidos
│   │   │       └── productos.html # Catálogo de productos
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py               # Configuración del administrador de Django
│   │   ├── apps.py                # Configuración de la aplicación
│   │   ├── models.py              # Modelos de Django
│   │   ├── tests.py               # Pruebas de la aplicación
│   │   ├── urls.py                # Rutas de la aplicación
│   │   └── views.py               # Lógica de las vistas
│   │
│   ├── db.sqlite3                 # Base de datos SQLite de Django
│   └── manage.py                  # Herramienta de administración de Django
│
├── .gitignore                     # Archivos excluidos de Git
├── README.md                      # Documentación del proyecto
├── requirements.txt               # Dependencias del proyecto
└── database.py                    # Archivo adicional de conexión/configuración


## URl de deploy de la api
```text

    URL: https://techgear-1-sxtj.onrender.com

```

