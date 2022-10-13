"""""""""""""""""""""
== compara os valores
= igual
>= maior que
<= menor que 
!= diferente
"""""""""""
nome =input('Qual o seu nome?')
idade= input('Qual a sua idade?')

idade= int(idade)

idade_min = 20
idade_max = 30

if idade >= idade_min and idade <= idade_max:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
