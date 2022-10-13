'''
crie uma função que receba o valor de outra função como parametro e retorne o valor da segunda função executada
'''

def func1(arg):
    print(arg)
def func2():
    x= 'Carlos'
    return x

var = func2()
func1(var)
"""
Crie uma função que receba o valor de outra função como parametro e retorne o valor da segunda função executada.
Faça a função 1 execuar duas funções que recebam um número diferente de argumentos.
"""

def mestre(funcao,*args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi,'Luiz')
executando2= mestre(saudacao, 'Luiz', saudacao = 'Bom dia!')
print(executando)
print(executando2)