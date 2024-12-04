from fastapi import FastAPI, HTTPException
from app.factories import VehicleFactory
from app.builders import VehicleBuilder
from app.proxies import ReservationProxy
from app.strategies import SimplePricingStrategy

app = FastAPI()

# Crear instancias de los patrones
factory = VehicleFactory()
pricing_strategy = SimplePricingStrategy()
proxy = ReservationProxy()

@app.get("/")
def read_root():
    return {"message": "Sistema de Reserva de Vehículos"}

@app.post("/reserve")
def reserve_vehicle(vehicle_type: str, duration: int):
    """
    Endpoint para reservar un vehículo.
    - `vehicle_type`: "bicycle" o "scooter".
    - `duration`: Duración de la reserva en horas.
    """
    try:
        # Crear el vehículo usando Factory Method
        vehicle = factory.create_vehicle(vehicle_type)
        
        # Calcular precio usando Strategy
        price = pricing_strategy.calculate_price(vehicle, duration)
        
        # Registrar la reserva usando Proxy
        reservation = proxy.reserve(vehicle, duration, price)
        return reservation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
