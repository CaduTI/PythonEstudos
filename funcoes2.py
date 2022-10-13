'''
funções em python, *args ** kwargs
'''

def func(*args, **kwargs):
    print(args, kwargs)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

'''
ambos os termos permitem o uso variável de argumentos em funções. Todavia, enquanto *args permite o uso de argumentos puramente posicionais (argumentos sem nome, um vetor de argumentos), **kwargs permite acrescentar argumentos nomeados em função (um dicionário de argumentos).
'''