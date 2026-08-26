from pydantic import BaseModel, Field


class Cliente(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100)
    telefono: str = Field(..., min_length=7, max_length=20)
    direccion: str = Field(..., min_length=5, max_length=200)
    ciudad: str = Field(..., min_length=2, max_length=100)


class Pedido(BaseModel):
    cliente: Cliente
    producto_id: str = Field(..., min_length=1)
    cantidad: int = Field(..., gt=0)
    total: float = Field(..., gt=0)