class Car:
    def init(self, make, color):
        self.make = make
        self.color = color


    def chanch_color(self, new_color):
        self.color = new_color


    def drive_to(self, destination):
        print(f"Driving to {destination}")

class ElectroCar(Car):
    def init(self, make, color):
        super().init(make, color)
        self.batarey = 100

    def drive_to(self, destination):
        if self.batarey > 5:
            print(f"Driving to {destination}")
        else:
            print(f"Driving not to {destination}")

    def chanch_batarey(self):
        print(f"идет заряд")
        self.batarey += 10
        if self.batarey >= 100:
            self.batarey = 100

tesla = ElectroCar("Tesla", "black")
print(f"Electro car is {tesla.make}, {tesla.color}")
tesla.drive_to("Кара балта")
tesla.chanch_batarey()
tesla.drive_to("Кара балта")