# Переменные класса
# Методы класса
# Статические методы класса

class User:
    #Переменные класса
    user_count = 0
    default_password = "123456789"

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.role = "user"
        self.password = User.default_password
        User.user_count += 1

    # Методы класса
    @classmethod
    def create_admin(cls, name, phone_number):
        new_admin = cls(name, phone_number)
        #new_admin = User(name,phone_number)→same the above
        new_admin.role = "admin"
        return new_admin

    @classmethod
    def get_user_count(cls):
        return User.user_count
       #return cls.user.count →same the above

    # Статические методы класса
    @staticmethod
    def validate_password(password):#Validate-Тастыктоо,Текшерүү
        # if len(password) < 8:
        #     return False
        # else:
        #     return True
        return len(password) >= 8

    # Методы экземпляра(обьекта)
    # Методы экземпляра(обьекта) нельзя вызывать внутри класса и внутри методов класса(потому что там сам класс)
    def change_password(self, password):
        if User.validate_password(password):
            self.password = password
        else:
            raise ValueError(f"Password is too short {self.name}")

print("Number of users:", User.user_count)
user_1 = User("Gul","0990567845")
print("Number of users:", User.user_count)
print(User.default_password)

admin_1 = User.create_admin("Ai", "0996451256")
print("Role of the user:", admin_1.role)
print("Number of users:", User.get_user_count())
admin_1.change_password("1")