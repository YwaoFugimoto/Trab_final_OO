class Date:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def set_day(self, day):
        self.day = day

    def get_month(self):
        return self.month

    def set_month(self, month):
        self.month = month

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

# Example usage:
if __name__ == "__main__":
    day = 25
    month = 7
    year = 2023

    date = Date(day, month, year)
    print(date)  # This will print the date in the format "day/month/year"
