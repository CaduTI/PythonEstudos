import requests
import json


def main():
    print('##################')
    print('###Pesquisa de CEP###')
    print('##################')

    cep = input('Digite um CEP válido:')

    if len(cep) != 8:
        print('Quantidade inválida de dígitos')
        exit()
    request = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(cep))
    address_data = request.json()
    print(address_data)
    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==')

        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))

    else:
        print('{}: CEP inválido.'.format(cep))

    print('---------------------------------')
    option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')


if __name__ == '__main__':
    main()
else:
    pass

'''if 'erro' not in adress_data:
    print('CEP Encontrado!!!')
    lista=['Cep','Logradouro','Complemento','Bairro','Cidade','Estado']
    retorno_lista= 
    for lista in range(0,6):
        for lista2 in range(0,6):
            print('{}: {}'.format(lista, adress_data[]))

'''
'''
Usar dois for para formatar e diminuir as linhas de impressão
'''