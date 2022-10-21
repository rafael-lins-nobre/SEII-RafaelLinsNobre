# ======= Codigo 1 ==========
try:
    f = open('test_file.txt')
    #var = bad_var # Causa um erro
except FileNotFoundError:
    print('Desculpa. Esse arquivo nao existe!')
except Exception as e:
    print(e)

# ======= Codigo 2 ==========
try:
    f = open('curruptfile.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executando...")

print('Fim do programa')