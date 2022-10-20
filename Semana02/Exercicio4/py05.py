# Key and Values / Hashmaps

student = {'name': 'Rafael', 'Age': 22, 'curso': ['mecatronica', 'aeronautica']}
          # Key  :  Value
print(student['name'])

student['phone'] = '82996388490' # pode ser usado para modificar o Valor de uma Key existente

idade = student.get('Age','Erro')
print(idade)
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, values in student.items():
    print(key,values)

