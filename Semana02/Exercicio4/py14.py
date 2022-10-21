import os

os.chdir("/home/rafael/Documents/sistemas_digitais/SEII-RafaelLinsNobre/Semana02/Exercicio4/Planetas_py14")
# print(os.getcwd())
# print(os.listdir())
# print('')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split('-')

    f_num = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    print(new_name)

    os.rename(f, new_name)