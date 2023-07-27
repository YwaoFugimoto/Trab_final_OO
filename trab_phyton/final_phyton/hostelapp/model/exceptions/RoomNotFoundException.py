class RoomNotFoundException(Exception):
    def __init__(self, message, number):
        super().__init__(message)
        self.number = number

# Example usage:
if __name__ == "__main__":
    try:
        room_number = "101"
        raise RoomNotFoundException("Room not found", room_number)
    except RoomNotFoundException as e:
        print(f"RoomNotFoundException: {e}")
        print(f"Room number: {e.number}")
