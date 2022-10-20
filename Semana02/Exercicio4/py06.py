from re import A


language = 'jav'

if language == 'python':
    print('Linguagem é python')
elif language == 'java':
    print('Linguagem é Java')
else:
    print('Sem correspondencia')
    
user = 'Rafael'
bool = True

if(user =='Rafael' and bool == True):
    print('Usuario checado')
    
a = 3
b = a
#a = 6
print(a is b)