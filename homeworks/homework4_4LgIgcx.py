class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        # Для соответствия примеру вывода можно также использовать атрибут phone:
        self.phone = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        # Проверяем, состоит ли номер только из цифр и ровно ли их 10
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        return False


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        # 1. Проверяем номер телефона с помощью метода класса Contact
        if Contact.validate_phone_number(phone_number):
            # 2. Если номер правильный - создаем новый объект Contact
            new_contact = Contact(name, phone_number)
            # 3. Добавляем этот новый объект в список all_contacts
            cls.all_contacts.append(new_contact)
        else:
            # Иначе вызываем ошибку в классе ContactList
            raise ValueError(
                f"Некорректный номер телефона: '{phone_number}'. Номер должен содержать ровно 10 цифр."
            )


class Library:

    def __init__(self, city, books=None):
        self.city = city
        # Если books не передан (None), создаем пустой список
        self.books = books if books is not None else []

    def __str__(self):
        return f"<Library object, city: {self.city}, books: {len(self.books)}>"

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        print(f"Ищем книгу: {item}")
        return item in self.books

    def __bool__(self):
        return len(self.books) > 5
print("--- Тестирование контактов ---")
print(ContactList.all_contacts)  # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)

try:
    ContactList.add_contact("John Doe", "5551234")
except ValueError as e:
    print("Ошибка перехвачена:", e)
print("\n--- Тестирование библиотеки ---")
lib = Library("Бишкек", books=["Война и мир", "1984", "Мастер и Маргарита"])
print(lib)
print(len(lib))
print("1984" in lib)
print("Гарри Поттер" in lib)

if lib:
    print("Библиотека большая (более 5 книг)")
else:
    print("Библиотека маленькая")