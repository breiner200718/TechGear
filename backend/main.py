from fastapi import FastAPI
from database import client, db

from routes.productos import router as productos_router
from routes.pedidos import router as pedidos_router

app = FastAPI(
    title="TechGear API",
    description="API para el sistema de catálogo y pedidos de TechGear",
    version="1.0.0"
)

app.include_router(productos_router)
app.include_router(pedidos_router)


@app.get("/")
def inicio():
    return {
        "mensaje": "API de TechGear funcionando"
    }


@app.get("/test-db")
def probar_database():
    try:
        client.admin.command("ping")

        return {
            "mensaje": "Conexión con MongoDB Atlas exitosa",
            "base_de_datos": db.name
        }

    except Exception as e:
        return {
            "mensaje": "Error de conexión con MongoDB Atlas",
            "error": str(e)
        }