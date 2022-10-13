"""class A:
    def falar(self):
        print("Falando.... estou em A")

class B(A):
    def falar(self):
        print("Falando.... estou em B")

class C(A):
    def falar(self):
        print("Falando.... estou em C")

class D(B,C):
    pass

d= D()
d.falar()"""
class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado= True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado= False
