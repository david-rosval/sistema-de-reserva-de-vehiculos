class PricingStrategy:
    def calculate_price(self, vehicle, duration: int) -> float:
        raise NotImplementedError

class SimplePricingStrategy(PricingStrategy):
    def calculate_price(self, vehicle, duration: int) -> float:
        return vehicle.base_price * duration
