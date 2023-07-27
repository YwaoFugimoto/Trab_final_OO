class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

class Reservation:
    def __init__(self, checkinDate=None, checkoutDate=None):
        self.reservationDate = Date()
        self.checkinDate = checkinDate
        self.checkoutDate = checkoutDate

    def get_reservation_date(self):
        return self.reservationDate

    def set_reservation_date(self, reservationDate):
        self.reservationDate = reservationDate

    def get_checkin_date(self):
        return self.checkinDate

    def set_checkin_date(self, checkinDate):
        self.checkinDate = checkinDate

    def get_checkout_date(self):
        return self.checkoutDate

    def set_checkout_date(self, checkoutDate):
        self.checkoutDate = checkoutDate

    def __str__(self):
        return f"Reservation{{reservationDate={self.reservationDate}, checkinDate={self.checkinDate}, checkoutDate={self.checkoutDate}}}"

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma instância de Date
    reservationDate = Date(2023, 7, 25)
    checkinDate = Date(2023, 8, 1)
    checkoutDate = Date(2023, 8, 8)

    # Criando uma instância de Reservation
    reservation = Reservation(checkinDate, checkoutDate)
    reservation.set_reservation_date(reservationDate)

    # Obtendo informações da reserva
    print("Data da reserva:", reservation.get_reservation_date().day, reservation.get_reservation_date().month, reservation.get_reservation_date().year)
    print("Data de check-in:", reservation.get_checkin_date().day, reservation.get_checkin_date().month, reservation.get_checkin_date().year)
    print("Data de check-out:", reservation.get_checkout_date().day, reservation.get_checkout_date().month, reservation.get_checkout_date().year)
