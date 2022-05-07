from airplain import plain


class War_Plain(plain.Plain):
    def __init__(self, weight, year, range_of_flight):
        super().__init__(weight, year, range_of_flight)
        self.passengers = 0

    def descriptor(self):
        print(F"ЭТОТ САМОЛЕТ имеет {self.passengers} пассажиров. ")