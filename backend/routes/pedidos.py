from fastapi import APIRouter, HTTPException
from schemas.pedido_schema import Pedido
from database import pedidos_collection
from bson import ObjectId

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)


@router.post("/")
def crear_pedido(pedido: Pedido):
    resultado = pedidos_collection.insert_one(
        pedido.model_dump()
    )

    return {
        "mensaje": "Pedido creado correctamente",
        "id": str(resultado.inserted_id)
    }


@router.get("/")
def obtener_pedidos():
    pedidos = list(pedidos_collection.find())

    for pedido in pedidos:
        pedido["_id"] = str(pedido["_id"])

    return pedidos


@router.get("/{pedido_id}")
def obtener_pedido(pedido_id: str):
    try:
        pedido = pedidos_collection.find_one(
            {"_id": ObjectId(pedido_id)}
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="ID de pedido inválido"
        )

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    pedido["_id"] = str(pedido["_id"])

    return pedido


@router.put("/{pedido_id}")
def actualizar_pedido(
    pedido_id: str,
    pedido: Pedido
):
    try:
        resultado = pedidos_collection.replace_one(
            {"_id": ObjectId(pedido_id)},
            pedido.model_dump()
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="ID de pedido inválido"
        )

    if resultado.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    return {
        "mensaje": "Pedido actualizado correctamente"
    }


@router.delete("/{pedido_id}")
def eliminar_pedido(pedido_id: str):
    try:
        resultado = pedidos_collection.delete_one(
            {"_id": ObjectId(pedido_id)}
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="ID de pedido inválido"
        )

    if resultado.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    return {
        "mensaje": "Pedido eliminado correctamente"
    }