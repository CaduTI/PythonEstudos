tupla = (1,2,3,4,5,6)
print(tupla)
#transformo a tupla(não pode ser alterada) em uma list(maleável)
tupla = list(tupla)
print(tupla)
#edito um número da lista
tupla[3]= 5860
print(tupla)

#transformo novamente em tupla
tupla = tuple(tupla)
print(tupla)
