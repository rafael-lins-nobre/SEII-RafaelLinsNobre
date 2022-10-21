import os
from datetime import datetime

#print(dir(os))

print(os.getcwd()) # printa o diretorio atual

os.chdir('/home/rafael/Documents/SO')
print(os.getcwd())
print(os.listdir())

#os.mkdir("OS-Demo-2") # mkdir() não consegue criar uma hieraquia de diretorios de uma vez so
#os.mkdir("OS-Demo-2/Sub-Dir-1")
os.makedirs("OS-Demo-2/Sub-Dir-1") # makedirs() consegue criar a hieraquia de diretorios em uma unica linha 
os.removedirs('OS-Demo-2/Sub-Dir-1') # remove diretorios
#os.rename('Trabalho Final', 'Banqueiro')
print(os.listdir())
print('')

print(os.stat('Atividade1.txt'))
mod_time = os.stat('Atividade1.txt').st_mtime
print('Mod time em formato legivel:', datetime.fromtimestamp(mod_time))
print('')

#for dirpath, dirnames, filenames in os.walk('/home/rafael/Documents'):   #generates a tuple of directory tree
#    print('Current Path:', dirpath)
#    print('Directories: ', dirnames)
#    print('Files: ', filenames)
#    print()

print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'teste01.txt')
print(file_path)


print(os.path.basename('/tmp/teste01.txt'))
print(os.path.dirname('/tmp/teste01.txt'))
print(os.path.split('/tmp/teste01.txt'))
print(os.path.splitext('/tmp/teste01.txt'))
print(os.path.exists('/tmp/teste01.txt'))
print(os.path.isdir('/home/rafael/Documents/sistemas_digitais'))
