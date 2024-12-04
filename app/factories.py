from typing import Union

class Vehicle:
    def __init__(self, name: str, base_price: float):
        self.name = name
        self.base_price = base_price

    def __str__(self):
        return f"{self.name} (Base Price: ${self.base_price})"

class Bicycle(Vehicle):
    def __init__(self):
        super().__init__("Bicycle", 5.0)

class Scooter(Vehicle):
    def __init__(self):
        super().__init__("Scooter", 10.0)

class VehicleFactory:
    def create_vehicle(self, vehicle_type: str) -> Union[Bicycle, Scooter]:
        """
        Crea un vehículo basado en el tipo.
        """
        if vehicle_type == "bicycle":
            return Bicycle()
        elif vehicle_type == "scooter":
            return Scooter()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")
