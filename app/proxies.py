class ReservationProxy:
    def __init__(self):
        self.reservations = []

    def reserve(self, vehicle, duration, price):
        reservation = {
            "vehicle": str(vehicle),
            "duration": duration,
            "price": price,
        }
        self.reservations.append(reservation)
        return reservation
