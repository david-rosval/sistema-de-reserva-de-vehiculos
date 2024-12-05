class ReservationProxy:
    def __init__(self):
        self.reservas = []

    def reservar(self, vehicle, duration, price):
        reserva = {
            "vehiculo": str(vehicle),
            "duracion": duration,
            "precio": price,
        }
        self.reservas.append(reserva)
        return reserva
