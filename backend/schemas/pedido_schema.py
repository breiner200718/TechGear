from pydantic import BaseModel, Field


class Pedido(BaseModel):
    cliente: str = Field(..., min_length=2, max_length=100)
    producto_id: str = Field(..., min_length=1)
    cantidad: int = Field(..., gt=0)
    total: float = Field(..., gt=0)