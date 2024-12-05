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

@app.post("/reservar")
def reservar_vehicle(tipo_vehiculo: str, duracion: int):
    """
    Endpoint para reservar un vehículo.
    - `tipo_vehiculo`: "bicycle" o "scooter".
    - `duracion`: Duración de la reserva en horas.
    """
    try:
        # Crear el vehículo usando Factory Method
        vehiculo = factory.crear_vehiculo(tipo_vehiculo)

        # Seleccionar estrategia de precios
        if duracion > 5:
            strategy = DiscountPricingStrategy()  # Estrategia con descuento
        else:
            strategy = SimplePricingStrategy()  # Estrategia básica
        
        # Calcular precio usando Strategy
        precio = strategy.calcular_precio(vehiculo, duracion)
        
        # Registrar la reserva usando Proxy
        reservation = proxy.reservar(vehiculo, duracion, precio)
        return reservation
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

builder = VehicleBuilder()

@app.post("/personalizar-reserva")
def customize_vehicle(tipo_vehiculo: str, duracion: int, agregar_canasta: bool = False, agregar_casco: bool = False):
    """
    Endpoint para personalizar un vehículo.
    - `tipo_vehiculo`: Tipo de vehículo ("bicicleta" o "scooter").
    - `agregar_canasta`: Si el vehículo debe incluir una canasta.
    - `agregar_casco`: Si el vehículo debe incluir un casco.
    """
    try:
        # Crear el vehículo base usando el Builder
        builder.crear_vehiculo(tipo_vehiculo)
        
        # Añadir configuraciones opcionales
        if agregar_canasta:
            builder.agregar_canasta()
        if agregar_casco:
            builder.agregar_casco()
        
        # Construir y retornar el vehículo configurado
        vehiculo = builder.build()

        # Seleccionar estrategia de precios
        if duracion > 5:
            strategy = DiscountPricingStrategy()  # Estrategia con descuento
        else:
            strategy = SimplePricingStrategy()  # Estrategia básica
        
        # Calcular precio usando Strategy
        precio = strategy.calcular_precio(vehiculo, duracion)
        
        # Registrar la reserva usando Proxy
        reserva = proxy.reservar(vehiculo, duracion, precio)
        return reserva
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))