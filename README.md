TechGear
Descripción

TechGear es una aplicación web para la gestión de productos y pedidos de una tienda de hardware y accesorios tecnológicos.

El proyecto está dividido en dos partes principales:

Backend: API desarrollada con FastAPI, encargada de los endpoints, validaciones y conexión con la base de datos.
Frontend: aplicación desarrollada con Django, encargada de las vistas, plantillas HTML y presentación de la información al usuario.

La aplicación utiliza MongoDB como base de datos para el backend y SQLite para la aplicación Django.

TechGear/
│
├── .venv/
│
├── techgear_api/
│   ├── routes/
│   ├── schemas/
│   ├── .env
│   ├── database.py
│   └── main.py
│
├── techgear_web/
│   ├── config/
│   ├── techgear/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── db.sqlite3
│   └── manage.py
│
├── .gitignore
├── README.md
└── requirements.txt




## URl de deploy de la api
```text

    URL: https://techgear-1-sxtj.onrender.com

```

