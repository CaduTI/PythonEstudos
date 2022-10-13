"""
Associação - Usa|| Agregação - Tem | Composição - é dono | Herança - É
"""


from poo_aula1 import pessoa

p1 = pessoa('Luiz', 29)
p1.comer('maçã')
p1.comer('maçã')
print(p1.idade)
p1.get_ano_nasc()
print(pessoa.gerar_id())
print(p1.gerar_id())

#################################################

from agregação import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

prod1 = Produto('Camiseta', 50)
prod2 = Produto('Iphone', 10000)
prod3 = Produto('Processador', 50)

carrinho.inserir_produto(prod1)
carrinho.inserir_produto(prod2)
carrinho.inserir_produto(prod3)

print(carrinho.soma_total())
##################################
"""from composição import Cliente, Endereco

cliente1= Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()

print()"""

##################################################
from Herança import*

c1 = Cliente('Luiz', 45)
print(c1.nome)