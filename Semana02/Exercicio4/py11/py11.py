# Forma mais simples de abrir. Nao sei pq nao estava reconhecendo o diretorio como o mesmo de test.txt 
# f = open('py11/test.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()
# print('')

# Abrindo arquivo com context manager
# with open('py11/test.txt', 'r') as f:
# 
#     print(f.name)
#     print(f.mode)
# 
#     f_contents = f.read()
#     print(f_contents)
#     
#     f_contents = f.readline()
#     print(f_contents, end='')
# 
#     print(f.closed)
# 
# print(f.closed)

# Loop "for" para printar as linhas
# with open('py11/test.txt', 'r') as f:
#    for line in f:
#        print(line, end='')

# with open('py11/test.txt', 'r') as f:
# 
#    size_to_read = 10
#    f_contents = f.read(size_to_read)
# 
#    while len(f_contents) > 0:
#        print(f_contents, end='')
#        f_contents = f.read(size_to_read) #at the end of the file f.read returns an empty string

# with open('py11/test.txt', 'r') as f:
# 
#    size_to_read = 10
#    f_contents = f.read(size_to_read)
#    print(f_contents, end = '')
# 
#    f.seek(0)
# 
#    f_contents = f.read(size_to_read)
#    print(f_contents)

# Copiando de um arquivo para o outro
# with open('py11/test.txt', 'r') as rf:
#    with open('py11/test_copy.txt', 'w') as wf:
#        for line in rf:
#            wf.write(line)

# Copiando imagem
with open('py11/hollowknight.jpg', 'rb') as rf:
    with open('py11/Hollow_knight_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)