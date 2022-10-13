lista = [
    ['P1', 13]
    ['P2', 5]
    ['P3', 3]
    ['P4', 1]
    ['P5', 90]
]

def func(item):
    return item[1]
"Podemos organizar a lista de diferentes formas, veja:"
#lista.sort(key = func, reverse=True)
#lista.sort(key = lambda item: item[1], reverse=True)
print(sorted(key = lambda item: item[0]))
print(lista)