from hostelapp.model import Hostel, Address, Room, RoomType, RoomNotFoundException

hostel = Hostel.get_hostel()
hostel.set_name("Hostel Sparkling Water")
hostel.set_phone("+(55) 35-91111-1123")
hostel.set_contact_email("sparkling_water@gmail.com")

address = Address()
address.set_address("Nightmare street, 13")
address.set_city("Caxambu")
address.set_country("Brazil")
address.set_zip_code("12-440-000")
address.set_state("MG")

hostel.set_address(address)

room1 = Room("101", "D. Leopoldina", 1)
room2 = Room("102", "D. Pedro", 1)
room3 = Room("301", "Dr. Viotti", 3)

room1.set_room_type(RoomType.SINGLE)
room2.set_room_type(RoomType.DOUBLE)
room3.set_room_type(RoomType.SINGLE)

room1.set_description("Pleasant room with balcony")
room2.set_description("Large room with an extra bed")
room3.set_description("Standard room without balcony")

room1.set_dimension(15.50)
room2.set_dimension(50)
room3.set_dimension(7.80)

hostel.add_room(room1)
hostel.add_room(room2)
hostel.add_room(room3)

try:
    print(hostel.get_room_by_number("101"))
except RoomNotFoundException as e:
    print(e)

