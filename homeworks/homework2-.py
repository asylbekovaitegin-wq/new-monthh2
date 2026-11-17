class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет, я работаю {self.profession}.")


class Classmate(Person):
    def __init__(self, name, age, profession, group_name):
        super().__init__(name, age, profession)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник, учусь в группе {self.group_name}, мне {self.age} лет, работаю {self.profession}.")


class Friend(Person):
    def __init__(self, name, age, profession, hobby):
        super().__init__(name, age, profession)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг, мне {self.age} лет, работаю {self.profession}, моё хобби — {self.hobby}.")


classmate_1 = Classmate("Бектур", 20, "программистом", "PY-22")
classmate_2 = Classmate("Атай", 19, "дизайнером", "UX-11")

friend_1 = Friend("Алмаз", 21, "инженером", "футбол")
friend_2 = Friend("Тимур", 22, "маркетологом", "музыка")

classmate_1.introduce()
classmate_2.introduce()
friend_1.introduce()
friend_2.introduce()