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

person_1=Person("Ali","1995-01-10","Manager",True)
person_2=Person("Ai","2000-01-10","Student",False)
person_3=Person("Bob","2005-01-10","Student",False)

print(person_1.name,person_1.birth_date,person_1.occupation,person_1.higher_education)
print(person_2.name,person_2.birth_date,person_2.occupation,person_2.higher_education)
print(person_3.name,person_3.birth_date,person_3.occupation,person_3.higher_education)

person_1.introduce()
person_2.introduce()
person_3.introduce()
