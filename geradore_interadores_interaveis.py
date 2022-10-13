import sys
import time
'''lista=[0,1,2,3,4,5]
print(next(lista))
print(hasattr(lista, '_iter'))
#um iteraval vc pode iterar sobre ele , mas n necessariamente ele é um interador(te dar um valor por vez)
# / Um interador lhe dá um valor por vez como vimos
lista2= list(range(100))
'''

def gerador():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r
# ou
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)
g= gera()
print(g)
#for v in g:
#   print(v)