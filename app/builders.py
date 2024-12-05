from app.factories import Bicicleta, Scooter  # Importar las clases desde factories.py

class VehicleBuilder:
    def __init__(self):
        self.vehicle = None

    def crear_vehiculo(self, vehicle_type: str):
        if vehicle_type == "bicicleta":
            self.vehicle = Bicicleta()
        elif vehicle_type == "scooter":
            self.vehicle = Scooter()
        else:
            raise ValueError("Tipo de vehículo no válido")
        return self

    def agregar_canasta(self):
        self.vehicle.name += " + Canasta"
        return self

    def agregar_casco(self):
        self.vehicle.name += " + Casco"
        return self

    def build(self):
        return self.vehicle
