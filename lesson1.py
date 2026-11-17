class Car:
    def init(self, make, color):
        self.make = make
        self.color = color

    def chanch_color(self, new_color):
        self.color = new_color

    def drive_to(self, destination):
        print(f"Driving to {destination}")


car_1 = Car("Audi", "red")
car_2 = Car("BMW", "blue")
print(car_1, car_2)
print(f"{car_1.make}, {car_1.color}")
print(f"{car_2.make}, {car_2.color}")

car_2.drive_to("Kara_kol")


class Man:
    def init(self, name, age, hp, rol):
        self.name = name
        self.age = age
        self.hp = hp
        self.rol = rol

    def to_do(self, jump, kill, run, wolk):
        print(f"Jumping {jump}")
        print(f"Killing {kill}")
        print(f"Run {run}")
        print(f"Wolk {wolk}")


man_1 = Man(
    name="Assyl",
    age=22,
    hp=120,
    rol="Soldier",
)

man_2 = Man(
    name="Can",
    age=20,
    hp=100,
    rol="Soldier",
)