# O basico de POO

class Primal:
    
    def __init__(self,name, age):
        self.name = name
        self.age = age
        #print("Welcome! {}".format(name))
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
        
    def set_age(self, age):
        self.age = age
        
    def add_one(self, x):
        return x +1
    
    def hello(self):
        print('Hello!')
 
# p1.hello()
# print(p1.add_one(3))
        
p1 = Primal('Rafael',22)
print(p1.name)
print(p1.get_age())
p2 = Primal('Arthur',19)
print(p2.get_name())
p2.set_age(30)
print(p2.get_age())
