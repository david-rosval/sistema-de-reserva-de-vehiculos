from pydantic import BaseModel

class ReservationRequest(BaseModel):
    vehiculo: str
    duracion: int
