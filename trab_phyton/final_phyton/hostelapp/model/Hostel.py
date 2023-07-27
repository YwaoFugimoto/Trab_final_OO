from typing import Set, List
from datetime import date

class Address:
    def __init__(self):
        self.address = ""
        self.zipCode = ""
        self.city = ""
        self.state = ""
        self.country = ""

class Room:
    def __init__(self, number, name, capacity):
        self.number = number
        self.name = name
        self.capacity = capacity

class Guest:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName
        self.address = Address()
        self.email = ""
        self.birthDate = date(1970, 1, 1)
        self.reservations = []
        self.title = None

class RoomNotFoundException(Exception):
    def __init__(self, message, number):
        super().__init__(message)
        self.number = number

class Hostel:
    def __init__(self):
        self.name = ""
        self.address = Address()
        self.phone = ""
        self.contactEmail = ""
        self.description = ""
        self.inaugurationDate = date(1970, 1, 1)
        self.rooms = set()
        self.guests = []

    def add_guest(self, guest: Guest):
        self.guests.append(guest)

    def get_all_guests(self):
        return self.guests

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address: Address):
        self.address = address

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def get_contact_email(self):
        return self.contactEmail

    def set_contact_email(self, contactEmail):
        self.contactEmail = contactEmail

    @staticmethod
    def get_hostel():
        return Hostel()

    def get_rooms(self):
        return self.rooms

    def set_rooms(self, rooms: Set[Room]):
        self.rooms = rooms

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_inauguration_date(self):
        return self.inaugurationDate

    def set_inauguration_date(self, inaugurationDate: date):
        self.inaugurationDate = inaugurationDate

    def get_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        raise RoomNotFoundException("Room not found! : ", number)

    def add_room(self, room: Room):
        self.rooms.add(room)

    def __str__(self):
        return f"Hostel{{name='{self.name}', address={self.address}, phone='{self.phone}', contactEmail='{self.contactEmail}', description='{self.description}', inaugurationDate={self.inaugurationDate}, rooms={self.rooms}}}"

# Exemplo de uso:
if __name__ == "__main__":
    # Criando uma instância de Address
    address = Address()
    address.address = "Rua dos Exemplos, 123"
    address.city = "Exemploville"
    address.country = "Brazil"
    address.zipCode = "12345-678"
    address.state = "EX"

    # Criando uma instância de Hostel
    hostel = Hostel()
    hostel.set_name("Exemplo Hostel")
    hostel.set_address(address)
    hostel.set_phone("(55) 35-91111-1123")
    hostel.set_contact_email("exemplo_hostel@example.com")
    hostel.set_description("Um ótimo lugar para se hospedar!")
    hostel.set_inauguration_date(date(2010, 5, 15))

    # Criando algumas instâncias de Room
    room1 = Room("101", "Quarto Individual", 1)
    room2 = Room("102", "Quarto Duplo", 2)

    # Adicionando os quartos ao Hostel
    hostel.add_room(room1)
    hostel.add_room(room2)

    # Criando uma instância de Guest
    guest = Guest("João", "Silva")
    guest.set_address(address)
    guest.email = "joao.silva@example.com"
    guest.birthDate = date(1990, 7, 10)

    # Adicionando o hóspede ao Hostel
    hostel.add_guest(guest)

    # Obtendo informações do Hostel
    print("Nome do Hostel:", hostel.get_name())
    print("Endereço do Hostel:", hostel.get_address().address)
    print("Telefone do Hostel:", hostel.get_phone())
    print("Email de contato do Hostel:", hostel.get_contact_email())
    print("Descrição do Hostel:", hostel.get_description())
    print("Data de inauguração do Hostel:", hostel.get_inauguration_date())

    # Obtendo informações dos quartos do Hostel
    print("\nQuartos disponíveis no Hostel:")
    for room in hostel.get_rooms():
        print(f"Número: {room.number}, Nome: {room.name}, Capacidade: {room.capacity}")

    # Obtendo informações dos hóspedes do Hostel
    print("\nHóspedes registrados no Hostel:")
    for guest in hostel.get_all_guests():
        print(f"Nome: {guest.firstName} {guest.lastName}, Email: {guest.email}, Data de Nascimento: {guest.birthDate}")
