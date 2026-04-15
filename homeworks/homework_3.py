from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    # # getter *method
    # def get_occupation(self):
    #     return self.__occupation

    # getter @property *attribute
    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def age(self):
        age = round((datetime.now() - datetime.strptime(self.__birth_date, "%Y-%m-%d")).days/365) #strptime() teksti date ailantuu
        return age

    def introduce(self):
        print (f"My name is {self.name}."
                f"I was born in {self.birth_date}."
                f"My occupation is {self.__occupation}."
                f"Higher education: {'Yes' if self.__higher_education else 'No'}")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, person_name):
        super().__init__(name, birth_date, occupation, higher_education)#super() used to get method or attribute from parent class to child
        self.person_name = person_name
        self.group_name = group_name

    def introduce(self):
       print(f"Hi, my name is {self.name}. "
             f"My occupation is {self.occupation}. "
             f"I am {self.person_name}'s classmate and our group name is {self.group_name}. "
             f"Higher education: {'Yes' if self.higher_education else 'No'}.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, person_name):#added extra attribute(person_name) to get main person's name
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.person_name = person_name

    def introduce(self):
       print(f"Hi, my name is {self.name}. My occupation is {self.occupation}. I'm {self.person_name}'s friend and my hobby is {self.hobby}. Higher education: {'Yes' if self.higher_education else 'No'}.")

person_1=Person("Alia", "2000-01-01", "Student", False)
classmate_1=Classmate("Ali", "2003-01-01", "Student", False, "65-1В27022026", person_1.name)
classmate_2=Classmate("Nur", "2005-01-01", "Student", False, "70-1В27022026", person_1.name)
friend_1=Friend("Bek", "2000-01-01", "Developer", True, "hiking", person_1.name)
friend_2=Friend( "Job", "2005-01-01", "Student", True, "swimming", person_1.name)

#Polymorphism (Көп түрдүүлүк)↓ using one method to different objects
people=[person_1, classmate_1, classmate_2, friend_1, friend_2]
for p in people:
   p.introduce()

print(f"{friend_2.name} has {friend_2.age} years old.")

#print(person_1.occupation) using @property
#print(person_1.get_occupation()) # through method getter
#print(person_1.__occupation) error, private bolgon uchun tuz access jok
