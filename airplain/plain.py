class Plain:
    def __init__(self, weight, year, range_of_flight):
        self.weight = weight
        self.year = year
        self.range_of_flight = range_of_flight


    def show_plain(self):
        print(f"{self.weight}, {self.year} год, {self.range_of_flight}")
