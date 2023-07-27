from typing import List

class Address:
    def __init__(self):
        self.address = ""
        self.zipCode = ""
        self.city = ""
        self.state = ""
        self.country = ""

class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

class Reservation:
    pass  # Implementar a classe Reservation se necessário

class Guest:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName
        self.address = Address()
        self.email = ""
        self.birthDate = Date()
        self.reservations = []
        self.title = None

    def getFirstName(self):
        return self.firstName

    def setName(self, name):
        if len(name) > 2:
            self.firstName = name
            return True
        return False

    def __str__(self):
        return f"{self.firstName}\t{self.lastName}\t{self.email}\t"

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getBirthDate(self):
        return self.birthDate

    def setBirthDate(self, birthDate):
        self.birthDate = birthDate

    def getReservations(self):
        return self.reservations

    def setReservations(self, reservations: List[Reservation]):
        self.reservations = reservations

    def addReservation(self, reservation: Reservation):
        self.reservations.append(reservation)

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma instância de Address
    address = Address()
    address.address = "Rua dos Exemplos, 123"
    address.city = "Exemploville"
    address.country = "Brazil"
    address.zipCode = "12345-678"
    address.state = "EX"

    # Criando uma instância de Date
    birthDate = Date(10, 7, 1990)

    # Criando uma instância de Guest
    guest = Guest("João", "Silva")
    guest.setAddress(address)
    guest.setEmail("joao.silva@example.com")
