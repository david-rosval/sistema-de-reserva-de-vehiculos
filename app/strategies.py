class PricingStrategy:
    """
    Clase base para las estrategias de cálculo de precios.
    Define la interfaz común para todas las estrategias.
    """
    def calculate_price(self, vehicle, duration: int) -> float:
        raise NotImplementedError("This method should be overridden in a subclass.")


class SimplePricingStrategy(PricingStrategy):
    """
    Estrategia básica: calcula el precio multiplicando el precio base del vehículo por la duración.
    """
    def calculate_price(self, vehicle, duration: int) -> float:
        return vehicle.base_price * duration


class DiscountPricingStrategy(PricingStrategy):
    """
    Estrategia con descuento: aplica un descuento del 20% si la reserva es de más de 5 horas.
    """
    def calculate_price(self, vehicle, duration: int) -> float:
        base_price = vehicle.base_price * duration
        if duration > 5:
            base_price *= 0.8  # Aplica un descuento del 20%
        return base_price


class DemandPricingStrategy(PricingStrategy):
    """
    Estrategia dinámica: incrementa el precio en un 50% durante alta demanda.
    """
    def __init__(self, high_demand: bool):
        self.high_demand = high_demand

    def calculate_price(self, vehicle, duration: int) -> float:
        base_price = vehicle.base_price * duration
        if self.high_demand:
            base_price *= 1.5  # Incrementa el precio en un 50% si hay alta demanda
        return base_price
