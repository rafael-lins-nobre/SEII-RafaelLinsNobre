# Usando multiplas classes em POO

import argparse


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []    
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        print("Numero máximo de estudantes atingido")
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value/len(self.students)

s1 = Student("Rafael", 22, 95)
s2 = Student("Arthur", 19, 80)
s3 = Student("Alex", 22, 65)

course = Course("Mcatronica", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name, course.students[1].name)
course.add_student(s3)

print(course.get_average_grade())