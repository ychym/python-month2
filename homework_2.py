class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f"My name is {self.name}.I was born in {self.birth_date}."
              f"My occupation is {self.occupation}."
              f"Higher education: {'Yes' if self.higher_education else 'No'}")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, person_name):
        super().__init__(name, birth_date, occupation, higher_education)#super() used to get method or attribute from parent class to child
        self.group_name = group_name
        self.person_name = person_name
    def introduce(self):
        print(f"Hi my name is {self.name}.I am {self.person_name}'s classmate and my group name is {self.group_name}.")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, person_name):#added extra attribute(person_name) to get main person's name
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.person_name = person_name
    def introduce(self):
       print(f"Hi, my name is {self.name}.I'm {self.person_name}'s friend and my hobby is {self.hobby}.")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, person_name, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby, person_name)
        self.shared_memory = shared_memory
    def introduce(self):
        super().introduce()
        #print(f"{super().introduce()}{self.shared_memory}")#double print()→NONE in the result
        print(self.shared_memory)

person_1=Person("Alia", "2000-01-01", "Student", True)
classmate_1=Classmate("Ali", "2003-01-01", "Student", False, "65-1В27022026", person_1.name)
classmate_2=Classmate("Nur", "2005-01-01", "Student", False, "70-1В27022026", person_1.name)
friend_1=Friend("Bek", "2000-01-01", "Developer", True, "hiking", person_1.name)
friend_2=Friend( "Job", "2005-01-01", "Student", False, "swimming", person_1.name)
bestfriend_1=BestFriend("Ai", "2005-01-01", "Student", False, "swimming", person_1.name, "I'VE KNOWN MY TWO BEST FRIENDS SINCE FROM 9TH GRADE.")

#Polymorphism (Көп түрдүүлүк)↓ using one method to different objects
people=[person_1, classmate_1, classmate_2, friend_1, friend_2, bestfriend_1]
for p in people:
   p.introduce()
