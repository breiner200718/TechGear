from fastapi import APIRouter, HTTPException
from schemas.producto_schema import Producto
from database import productos_collection

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)


@router.post("/")
def crear_producto(producto: Producto):
    resultado = productos_collection.insert_one(producto.model_dump())

    return {
        "mensaje": "Producto creado correctamente",
        "id": str(resultado.inserted_id)
    }


@router.get("/")
def obtener_productos():
    productos = list(productos_collection.find())

    for producto in productos:
        producto["_id"] = str(producto["_id"])

    return productos


@router.get("/{producto_id}")
def obtener_producto(producto_id: str):
    from bson import ObjectId

    try:
        producto = productos_collection.find_one({
            "_id": ObjectId(producto_id)
        })
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="ID de producto inválido"
        )

    if not producto:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    producto["_id"] = str(producto["_id"])

    return producto


@router.put("/{producto_id}")
def actualizar_producto(producto_id: str, producto: Producto):
    from bson import ObjectId

    try:
        resultado = productos_collection.replace_one(
            {"_id": ObjectId(producto_id)},
            producto.model_dump()
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="ID de producto inválido"
        )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {
        "mensaje": "Producto actualizado correctamente"
    }


@router.delete("/{producto_id}")
def eliminar_producto(producto_id: str):
    from bson import ObjectId

    try:
        resultado = productos_collection.delete_one({
            "_id": ObjectId(producto_id)
        })
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="ID de producto inválido"
        )

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {
        "mensaje": "Producto eliminado correctamente"
    }