
#tenho que cria uma lista contendo os ids das
def ordenar_id():
    lista_legal_entity = [94562, 93579, 96123, 984567, 12348, 56789, 43879, 89334, 16137, 42241, 64736, 31651, 62578,
                          32974, 87313, 74202, 75371, 51802, 56251, 79259, 30323, 77767, 46197, 91186, 89756, 89941,
                          44541, 2907, 93172, 25536, 81153, 91394, 47839, 46215, 59650, 42967, 34159, 82739, 32302,
                          50295, 24980, 97037, 81945, 87557, 30011, 69259, 61760, 5383, 21062, 18011, 84642, 51385,
                          95778, 30839, 42571, 85534, 20781, 17247, 9168, 18913, 21156, 11934, 542, 21157]

    tupla_baterias_moura = (17247, 9168, 18913, 21156, 11934, 542, 21157)
    l = []
    for i in lista_legal_entity:
        for k in tupla_baterias_moura:
            if i== k:
                lista_legal_entity[0]
                l = lista_legal_entity[i]
            #x.insert(x.index('password2'),  x.pop(x.index('password2')+1))
            print(lista_legal_entity.index(17247))

ordenar_id()

test_list = ['title', 'email', 'password2', 'password1', 'first_name',
                 'last_name', 'next', 'newsletter']
reorder_func = lambda x: x.insert(x.index('password2'),  x.pop(x.index('password2')+1))
reorder_func(test_list)
print(test_list)

