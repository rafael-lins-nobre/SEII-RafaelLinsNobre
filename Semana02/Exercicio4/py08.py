
def hello(greeting, name = 'You'):
    return '{}, {}!'.format(greeting, name)

#print(hello('Hello', 'rafael'))

def info(*args, **kwargs):
    print(args)
    print(kwargs)
    
info('Math', 'Arts', name = 'rafael', age = 22)
print('')

courses = ['Math', 'Arts']
dados = {'name': 'rafael', 'age': 22}

info(*courses, **dados)