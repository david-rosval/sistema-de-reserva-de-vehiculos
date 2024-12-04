from app.factories import Bicycle, Scooter  # Importar las clases desde factories.py

class VehicleBuilder:
    def __init__(self):
        self.vehicle = None

    def create_vehicle(self, vehicle_type: str):
        if vehicle_type == "bicycle":
            self.vehicle = Bicycle()
        elif vehicle_type == "scooter":
            self.vehicle = Scooter()
        else:
            raise ValueError("Invalid vehicle type")
        return self

    def add_basket(self):
        if self.vehicle.name == "Bicycle":
            self.vehicle.name += " with Basket"
        return self

    def add_helmet(self):
        self.vehicle.name += " + Helmet"
        return self

    def build(self):
        return self.vehicle
