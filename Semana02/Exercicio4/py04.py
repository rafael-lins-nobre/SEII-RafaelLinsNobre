materias = ['Dinamica', 'Estatica', 'Otica', 'SO']

print(materias)
print(materias[2])
print(materias[-1])
print('Print intervalo:',materias[0:2]) # Primeira indxação é inclusiva, mas a segunda não

materias.append('Psicologia')
print('Add no final:',materias)

materias.insert(2,'MecSol')
print('INserção:', materias)
print('')

cursos = ['mecatronica', 'aeronautica']
materias.extend(cursos)
print('Fundindo listas:',materias)
print('')

materias.remove('SO')
print(materias)
popped = materias.pop()
print(popped)
print('')

materias.reverse()
print('Reverso:', materias)
print('')

materias.sort()  # Funciona para listas de número, ordena em ordem ascendente
# Existe um parâmetro para sort() que reverte a ordem: sort(reverse = true)
materias_sorted = sorted(materias)
print('Alfabetico:',materias_sorted)
print('Alfabetico:', materias)
print('')

# Funções min(),max() e sum() se aplicam a lists

print('Index de um elemento:', materias.index('Otica'))
print('Artes' in materias)
print('Estatica' in materias)
print('')

for index,item in enumerate(materias,start= 2):
    print(index,item)
print('')

materias_str = ', '.join(materias)
print('String da lista:',materias_str)
nova_lista = materias_str.split(', ')
print('nova lista:',nova_lista)
print('')

# Tuples nao sao mutaveis, enquanto lists sao, portanto possuem todas as funcionalidades que nao
# envolvem alteração dos dados.
# Tuples são criados com parenteses(): tuple = (1, 2, 4, 7)

# Sets são estruturas similares, porem eles nao se importam com a ordem dos dados dentro deles
# Usados comumente para eliminar dados duplicados e para verificar se há um dado especifico no set
# Sets sao criados usando chaves{}: set = {2, 5, 7, 9}

cs_courses = {'History', 'Math', 'Art', 'AOC'}
other_course = {'History', 'Math', 'what', 'idk'}
print(cs_courses.intersection(other_course))
print(cs_courses.difference(other_course))
print(cs_courses.union(other_course))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()