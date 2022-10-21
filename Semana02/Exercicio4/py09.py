#import modulo_py09 as mod
#from modulo_py09 import find_index, test
#from modulo_py09 import find_index as fi, test

import sys
sys.path.append('/home/rafael/Documents/sistemas_digitais/SEII-RafaelLinsNobre/Semana02/Exercicio3/')
from modulo_py09 import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Physics')
print(index)
print(test)


import random
random_course = random.choice(courses)
print(random_course)


import math
rads = math.radians(90)
print(math.sin(rads))


import datetime
import calendar

today = datetime.date.today()
print(today)
print(calendar.isleap(2022))


import os
print(os.getcwd())
print(os.__file__)