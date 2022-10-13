'''
criar uma funcao com dois paramentros: saudacao e nome.
'''

def saudacoes(saudacao,nome):
    print(saudacao, nome)

retorno = saudacoes('Olá, seja bem vindo','Carlos!')

'''
criar uma funçao que registre 3 números e exiba soma entre eles
'''

def soma(n1,n2,n3):
    print(n1 +n2+n3)

soma(6,4,5)
'''
criar uma funçao que tenha um número e uma porcentaghem, dps retorne o número e sua soma com a porcentagem indicada
'''

def calculo(n,p):
    print(n)
    print(n + n * p / 100)

calculo(6,10)

'''
Fizzbuzz- se o parametro da funçao for divisível por 3 retornar o "fizz", se divisível por 5 retorn "buzz", se for tanto por 5 e 3 retorne" fizzbuzz"
'''

def fizzbuzz(n):
    if n % 3 == 0 and n % 5== 0:
        print('FizzBuzz')
    if n % 3:
        print('Fizz')
    if n % 5:
        print('Buzz')

fizzbuzz(15)

