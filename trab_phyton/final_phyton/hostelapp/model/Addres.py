class Address:
    def __init__(self):
        self.address = ""
        self.zipCode = ""
        self.city = ""
        self.state = ""
        self.country = ""

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_zipCode(self):
        return self.zipCode

    def set_zipCode(self, zipCode):
        self.zipCode = zipCode

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def __str__(self):
        return f"Address{{address='{self.address}', zipCode='{self.zipCode}', city='{self.city}', state='{self.state}', country='{self.country}'}}"


# Example usage:
if __name__ == "__main__":
    address = Address()
    address.set_address("123 Main Street")
    address.set_zipCode("12345")
    address.set_city("Example City")
    address.set_state("Example State")
    address.set_country("Example Country")

    print(address)  # This will print the address information
