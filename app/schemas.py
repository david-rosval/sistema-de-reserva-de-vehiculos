from pydantic import BaseModel

class ReservationRequest(BaseModel):
    vehicle_type: str
    duration: int
