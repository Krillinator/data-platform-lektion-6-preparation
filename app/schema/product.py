from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    price: float
    quantity: int
    currency: str  # ISO 4217, "SEK", "EUR", "USD"