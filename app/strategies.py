class PricingStrategy:
    """
    Clase base para las estrategias de cálculo de precios.
    Define la interfaz común para todas las estrategias.
    """
    def calcular_precio(self, vehiculo, duracion: int) -> float:
        raise NotImplementedError("This method should be overridden in a subclass.")


class SimplePricingStrategy(PricingStrategy):
    """
    Estrategia básica: calcula el precio multiplicando el precio base del vehículo por la duración.
    """
    def calcular_precio(self, vehiculo, duracion: int) -> float:
        return vehiculo.precio_base * duracion


class DiscountPricingStrategy(PricingStrategy):
    """
    Estrategia con descuento: aplica un descuento del 20% si la reserva es de más de 5 horas.
    """
    def calcular_precio(self, vehiculo, duracion: int) -> float:
        precio_base = vehiculo.precio_base * duracion
        if duracion > 5:
            precio_base *= 0.8  # Aplica un descuento del 20%
        return precio_base


