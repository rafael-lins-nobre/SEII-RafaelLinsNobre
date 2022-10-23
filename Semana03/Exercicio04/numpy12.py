import numpy as np

# Funcoes de data science e eixos(axis)

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)
print(a.sum(axis=None)) # soma geral
print(a.sum())          # soma geral
print(a.sum(axis=0)) # ao longo das linhas -> 1 soma para cada coluna
print(a.sum(axis=1)) # ao longo das colunas -> 1 soma para cada linha

print(a.mean(axis=None)) # media geral
print(a.mean())          # media geral
print(a.mean(axis=0)) # ao longo das linhas -> 1 media para cada coluna
print(a.mean(axis=1)) # ao longo das colunas -> 1 media para cada linha

# Mais funcoes nao mencionadas: std, var, min, max