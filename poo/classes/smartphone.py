from eletronico import Eletronico

class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)#referencia ao atributo declarado na classe pai
        self._conectado = False

def conectar():
    pass
