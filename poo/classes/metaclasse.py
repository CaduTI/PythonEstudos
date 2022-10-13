class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'falab' not in namespace:
            print(f'oops, vc precisa criar o método falarb em {name}')

        else:
            if not callable(namespace['falarb']):
                print(f'falarb precisa ser um método, por favor valide o código!')
        print(namespace)

class A(metaclass=Meta):
    def falar(self):
        self.falarb()



class B(A):
    def falarb(self):
        print('Falando.......B......')
