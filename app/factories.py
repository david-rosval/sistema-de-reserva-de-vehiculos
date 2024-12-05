from typing import Union

class Vehiculo:
    def __init__(self, name: str, precio_base: float):
        self.name = name
        self.precio_base = precio_base

    def __str__(self):
        return f"{self.name} (Precio base: S/.{self.precio_base})"

class Bicicleta(Vehiculo):
    def __init__(self):
        super().__init__("Bicicleta", 5.0)

class Scooter(Vehiculo):
    def __init__(self):
        super().__init__("Scooter", 10.0)

class VehicleFactory:
    def crear_vehiculo(self, tipo_vehiculo: str) -> Union[Bicicleta, Scooter]:
        """
        Crea un vehículo basado en el tipo.
        """
        if tipo_vehiculo == "bicicleta":
            return Bicicleta()
        elif tipo_vehiculo == "scooter":
            return Scooter()
        else:
            raise ValueError(f"Tipo de vehículo desconocido: {tipo_vehiculo}")
