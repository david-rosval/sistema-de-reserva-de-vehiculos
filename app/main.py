from fastapi import FastAPI, HTTPException
from app.factories import VehicleFactory
from app.builders import VehicleBuilder
from app.proxies import ReservationProxy
from app.strategies import SimplePricingStrategy, DiscountPricingStrategy


app = FastAPI()

# Crear instancias de los patrones
factory = VehicleFactory()
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

        # Seleccionar estrategia de precios
        if duration > 5:
            strategy = DiscountPricingStrategy()  # Estrategia con descuento
        else:
            strategy = SimplePricingStrategy()  # Estrategia básica
        
        # Calcular precio usando Strategy
        price = strategy.calculate_price(vehicle, duration)
        
        # Registrar la reserva usando Proxy
        reservation = proxy.reserve(vehicle, duration, price)
        return reservation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

builder = VehicleBuilder()

@app.post("/customize-reservation")
def customize_vehicle(vehicle_type: str, duration: int, add_basket: bool = False, add_helmet: bool = False):
    """
    Endpoint para personalizar un vehículo.
    - `vehicle_type`: Tipo de vehículo ("bicycle" o "scooter").
    - `add_basket`: Si el vehículo debe incluir una canasta.
    - `add_helmet`: Si el vehículo debe incluir un casco.
    """
    try:
        # Crear el vehículo base usando el Builder
        builder.create_vehicle(vehicle_type)
        
        # Añadir configuraciones opcionales
        if add_basket:
            builder.add_basket()
        if add_helmet:
            builder.add_helmet()
        
        # Construir y retornar el vehículo configurado
        vehicle = builder.build()

        # Seleccionar estrategia de precios
        if duration > 5:
            strategy = DiscountPricingStrategy()  # Estrategia con descuento
        else:
            strategy = SimplePricingStrategy()  # Estrategia básica
        
        # Calcular precio usando Strategy
        price = strategy.calculate_price(vehicle, duration)
        
        # Registrar la reserva usando Proxy
        reservation = proxy.reserve(vehicle, duration, price)
        return reservation
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))