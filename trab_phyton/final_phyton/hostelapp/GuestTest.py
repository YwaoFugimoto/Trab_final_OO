class Address:
    def __init__(self):
        self.address = ""
        self.zipCode = ""
        self.city = ""
        self.state = ""
        self.country = ""

class RoomType:
    SINGLE = "Single"
    DOUBLE = "Double"

class Room:
    def __init__(self, number, name, capacity):
        self.number = number
        self.name = name
        self.capacity = capacity
        self.roomType = None
        self.description = ""
        self.dimension = 0.0

class Hostel:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.contactEmail = ""
        self.address = Address()
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        raise RoomNotFoundException("Room not found", number)

    @staticmethod
    def get_hostel():
        return Hostel()

class RoomNotFoundException(Exception):
    def __init__(self, message, number):
        super().__init__(message)
        self.number = number

# Example usage:
if __name__ == "__main__":
    hostel = Hostel.get_hostel()
    hostel.name = "Hostel Sparkling Water"
    hostel.phone = "+(55) 35-91111-1123"
    hostel.contactEmail = "sparkling_water@gmail.com"

    address = Address()
    address.address = "Nightmare street, 13"
    address.city = "Caxambu"
    address.country = "Brazil"
    address.zipCode = "12-440-000"
    address.state = "MG"

    hostel.address = address

    room1 = Room("101", "D. Leopoldina", 1)
    room2 = Room("102", "D. Pedro", 1)
    room3 = Room("301", "Dr. Viotti", 3)

    room1.roomType = RoomType.SINGLE
    room2.roomType = RoomType.DOUBLE
    room3.roomType = RoomType.SINGLE

    room1.description = "Pleasant room with balcony"
    room2.description = "Large room with an extra bed"
    room3.description = "Standard room without balcony"

    room1.dimension = 15.50
    room2.dimension = 50
    room3.dimension = 7.80

    hostel.add_room(room1)
    hostel.add_room(room2)
    hostel.add_room(room3)

    try:
        print(hostel.get_room_by_number("101"))
    except RoomNotFoundException as e:
        print(e)
