class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        return len(phone_number) >= 10

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            cls.all_contacts.append(Contact(name, phone_number))
        else:
            raise ValueError(f"Phone number is too short")

class Library:
    def __init__(self, city, books = None):
        self.city = city
        self.books = books

    def __str__(self):
        return f"<Library object, city: {self.city}, books: {self.books}>"

    def __len__(self):
        return len(self.books)

    def __contains__(self, item):
        print(f"{item} is in library")
        return item in self.books

    def __bool__(self):
        return len(self.books) > 5

ContactList.add_contact("Ai", "+1 555 555 555")
ContactList.add_contact("Billy", "+1 555 555 555")
for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)
#ContactList.add_contact("Billy", "+1 555")

library = Library("Bishkek", ["Ak Keme", "Harry Potter", "Ant"])
print(library)
print(len(library))
print("Ant" in library)
print("Ikigai" in library)

if library:
    print(f"Books are more than 5")
else:
    print(f"Books are less than 5")
