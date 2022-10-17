
mensagem_composta = '''Hello World
Estou vivo!'''
mensagem = "Hello World"
print(mensagem)
print(len(mensagem))
print("Caracter especifico:", mensagem[6])
print(mensagem[0:5])
print(mensagem.lower())
print(mensagem.upper())
print("Contagem de iterações:", mensagem.count('l'))
print("Achando posicao de string:", mensagem.find('World'))

nova_messagem = mensagem.replace('World', 'Universe')
print("Nova mensagem:", nova_messagem)

greeting = "Hello"
name = "Rafael"

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting,name)
print(message)
