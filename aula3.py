nome = 'Carlos'
idade = 21
altura = 1.75
peso = 86
imc = peso/(altura**2)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
"Outras formas de formatação do mesmo Print:"
print('{} tem {} anos de idade e seu IMC é {}'. format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im}'. format(n=nome, i=idade, im=imc))
"DESAFIO!!"
nome = 'Carlos'
Idade = 21
altura = 1.75
peso= 86
ano = 2021

nascimento= ano- idade
imc= peso/(altura**2)

print('{} tem {} anos de idade , {}m de altura e pesa {}KG'.format(nome, idade, altura, peso))
print('{} nasceu em {}'.format(nome, nascimento))
print('O IMC de {} é de {}'.format(nome, imc))