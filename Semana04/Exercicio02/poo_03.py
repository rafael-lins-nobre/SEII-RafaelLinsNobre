# Heranças e hierarquias de classe

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"Meu nome é {self.name} e eu tenho {self.age} anos.")
        
    def speak(self):
        print("Nao sei que animal eu sou!")
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("Meow!")
    
    def show(self):
        print(f"Meu nome é {self.name} e eu tenho {self.age} anos, minha cor é {self.color}.")

class Dog(Pet):
    def speak(self):
        print("Bark!")
        
p = Pet("Aiko", 8)
p.show()
p.speak()

c = Cat("Frida", 3, "Branca")
c.show()
c.speak()

d = Dog("Teo", 10)
d.show()
d.speak()