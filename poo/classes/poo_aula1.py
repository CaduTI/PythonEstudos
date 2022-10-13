#self na função referencia a instância, cls se refere a classe
#Tipos de métodos : por intância(self), da clase(método) e o estático
from random import randint
class pessoa:
    ano_atual= 2022
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade= idade

    def get_ano_nasc(self):
        print(self.ano_atual - self.idade)
    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod
    def gerar_id():
        rand = randint(10000, 999999)
        return rand

    def __init__(self, nome, idade, comendo= False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo= comendo
        self.falando= falando
    def comer(self,alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        if self.falando:
            print(f'{self.nome} não pode falar comendo porco do krl')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto):
        if self. comendo:
            print(f'{self.nome} nõ pode falar comendo! Mais educação!!')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando= False

p1 = pessoa('Luiz', 29)
p1.comer('maçã')
p1.comer('maçã')
print(p1.idade)
p1.get_ano_nasc()
print(pessoa.gerar_id())
print(p1.gerar_id())