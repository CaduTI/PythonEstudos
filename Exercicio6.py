string = '012345678901234567890123456789'
n = 10
#aplico o fatiamento com 'string[i:i +n]'
lista = [string[i:i +n] for i in range(0, len(string), n)]
#altero a vírgula pelo ponto
retorno = '.'.join(lista)

print(lista)
print(retorno)