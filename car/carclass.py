# from car import electrocar
#
class CarClass:
    def __init__(self, brand, model, year, probeg):
        self.brand = brand
        self.model =model
        self.year = year
        self.probeg = probeg

    def show_car(self):
        print(f"{self.brand}, {self.model}, {self.year}, {self.probeg}")
#
#
# if __name__ == '__main__':
#     e_car = electrocar.ElectroCar("Tesla", "T", 2022, 1199000)
#     e_car.show_car()
#     e_car.description_battery()