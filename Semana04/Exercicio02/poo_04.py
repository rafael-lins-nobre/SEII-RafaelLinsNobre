# Atributos de classe

class Person:
    number_of_people = 0
    
    def __init__(self,name):
        self.name = name
        #Person.number_of_people += 1
        Person.add_person()
    
    @classmethod
    def number(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        
p1 = Person("Rafael")
print(Person.number_of_people)
p2 = Person("Arthur")
print(Person.number_of_people)

print(Person.number())

#Person.number = 5
#print(p2.number)