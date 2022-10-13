"""perguntas = {
    'Pergunta 1' :{
        'pergunta' : 'Quanto é 2+2?',
        'respostas' :{
            'a' : '1',
            'b' : '4',
            'c' : '5'
        },
        'resposata_certa' : 'b',
    },
    'Pergunta 2' :{
        'pergunta' : 'Quanto é 3*2?',
        'respostas' :{
            'a' : '4',
            'b' : '10',
            'c' : '6'
        },
        'resposata_certa' : 'c',
    },
}
print()
respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta} : {dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, resposta_valor in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {resposta_valor}')

    resposta_usuario= input('sua resposta: ')

    if resposta_usuario == dados_pergunta['respostas_certas']:
        print('Parabéns! você acertou a pergunta!')
        respostas_certas += 1
    else:
        print('Errado! resposta incorreta')
    print()"""
print()
print('Texto explicativo')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('EHHHHHH!!! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('IXXIIIII!!! Você ERROU!!!!')

    print()
quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')

"""
print()

respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('EHHHHHH!!! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('IXXIIIII!!! Você ERROU!!!!')

    print()
"""