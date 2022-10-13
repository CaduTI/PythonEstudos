"""
public, private, protected
_ protected - uso somente na classe, algo semelhante ao private no java
__ private - encapsulo ela na claase, defino como não mexer nela em outro lugar que n seja sua classe
"""

class BaseDeDados:
    def __init__(self):
        self._dados = {}
    @property
    def getdados(self):
        return self._dados
    def inserir_cliente(self,id, nome):
        if 'cliente' not in self._dados:
            self._dados['clientes'] = {id : nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)
    def apaga_cliente(self,id):
        del self._dados ['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Otavio')
bd.inserir_cliente(2,'Miranda')
bd.inserir_cliente(3,'Lucas')
bd.apaga_cliente(3)
print(bd._dados)