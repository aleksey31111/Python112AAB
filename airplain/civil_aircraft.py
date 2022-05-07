from airplain import plain

class Civil_Plain(plain.Plain):
    def __init__(self, weight, year, range_of_flight):
        super().__init__(weight, year, range_of_flight)
        self.passengers = 1000

    def descriptor(self):
        print(F"ЭТОТ САМОЛЕТ имеет {self.passengers} Пасажиров. ")


if __name__ == '__main__':
    c_plain = Civil_Plain(10, 10, 10)
    c_plain.show_plain()
    c_plain.descriptor()
