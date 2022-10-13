from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError("Saldo deve ser númerico")
        self._saldo = valor

    def depositar(self, valor):
        if isinstance(valor, (int, float)):
            raise ValueError("Saldo deve ser númerico")
        self._saldo += valor
        self.detalhes_deposito()

    def detalhes_deposito(self):
        print(f'Agencia: {self._agencia}' 
              f'Conta: {self._conta}' 
              f'Saldo: {self._saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes_deposito()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self._saldo + self.limite) < valor:
            print('limite de saque ultrapassado')
            return
        self.saldo -= valor
        self.detalhes_deposito()
