from itertools import zip_longest, count
cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']
estados = ['SP', 'MG', 'BA', 'RJ']
indice = count()

estado_capital = zip(indice, estados, cidades)
print(estado_capital)
print("Ao usarmos a função {zip} unimos iteráveis em uma única variável, no caso o o formato fica como um gerador\n")
print(list(estado_capital))
print("Agr realizamos a conversão para o formato de dicionário")

############################
estado_capitalziplongest = zip_longest(indice, estados, cidades, fillvalue='Estado')
print(tuple(estado_capitalziplongest))

for c in estado_capital:
    print(c)
