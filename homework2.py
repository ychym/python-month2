class Person:
    def __init__(self,name,birth_date,occupation,higher_education):
        self.name=name
        self.birth_date=birth_date
        self.occupation=occupation
        self.higher_education=higher_education
    def introduce(self):
        print(f"My name is {self.name}.I was born in {self.birth_date}."
              f"My occupation is {self.occupation}."
              f"Higher education: {"Yes" if self.higher_education==True else "No"}")

class Classmate(Person):
    def __init__(self,name,birth_date,occupation,higher_education,group_name,person_name):
        super().__init__(name,birth_date,occupation,higher_education)#super() used to get method or attribute from parent class to child
        self.group_name=group_name
        self.person_name=person_name
    def introduce(self):
        print(f"Hi my name is {self.name}.I am {self.person_name}'s classmate and my group name is {self.group_name}.")

class Friend(Person):
    def __init__(self,name,birth_date,occupation,higher_education,hobby,person_name):#added extra attribute(person_name) to get main person's name
        super().__init__(name,birth_date,occupation,higher_education)
        self.hobby=hobby
        self.person_name=person_name
    def introduce(self):
       print(f"Hi, my name is {self.name}.I'm {self.person_name}'s friend and my hobby is {self.hobby}.")

class Bestfriend(Friend):
    def __init__(self,name,birth_date,occupation,higher_education,hobby,person_name,shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby, person_name)
        self.shared_memory=shared_memory
    def introduce(self):
        super().introduce()
        #print(f"{super().introduce()}{self.shared_memory}")#double print()→NONE in the result
        print(self.shared_memory)

person_1=Person(name="Alia",birth_date="2000-01-01",occupation="Student",higher_education=True)
classmate_1=Classmate(name="Ali",birth_date="2003-01-01",occupation="Student",higher_education=False,group_name="65-1В27022026",person_name=person_1.name)
classmate_2=Classmate(name="Nur",birth_date="2005-01-01",occupation="Student",higher_education=False,group_name="70-1В27022026",person_name=person_1.name)
friend_1=Friend(name="Bek",birth_date="2000-01-01",occupation="Developer",higher_education=True,hobby="hiking",person_name=person_1.name)
friend_2=Friend(name="Job",birth_date="2005-01-01",occupation="Student",higher_education=False,hobby="swimming",person_name=person_1.name)
bestfriend_1=Bestfriend(name="Ai", birth_date="2005-01-01", occupation="Student", higher_education=False, hobby="swimming", person_name=person_1.name, shared_memory="I'VE KNOWN MY TWO BEST FRIENDS SINCE FROM 9TH GRADE.")

#Polymorphism (Көп түрдүүлүк)↓
people=[person_1, classmate_1, classmate_2, friend_1, friend_2, bestfriend_1]
for p in people:
   p.introduce()
