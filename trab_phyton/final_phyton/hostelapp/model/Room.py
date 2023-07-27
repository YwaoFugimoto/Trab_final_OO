class Room:
    def __init__(self, number, name, floor):
        self.number = number
        self.name = name
        self.floor = floor
        self.description = ""
        self.dimension = 0.0
        self.roomType = None
        self.dailyRate = 0.0

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_floor(self):
        return self.floor

    def set_floor(self, floor):
        self.floor = floor

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_dimension(self):
        return self.dimension

    def set_dimension(self, dimension):
        self.dimension = dimension

    def get_room_type(self):
        return self.roomType

    def set_room_type(self, roomType):
        self.roomType = roomType

    def get_daily_rate(self):
        return self.dailyRate

    def set_daily_rate(self, dailyRate):
        self.dailyRate = dailyRate

    def __eq__(self, other):
        if not isinstance(other, Room):
            return False
        return self.floor == other.floor and self.number == other.number and self.name == other.name and self.roomType == other.roomType

    def __hash__(self):
        return hash((self.number, self.name, self.floor, self.roomType))

    def __str__(self):
        return f"Room{{number='{self.number}', name='{self.name}', floor={self.floor}, description='{self.description}', dimension={self.dimension}, roomType={self.roomType}}}"
