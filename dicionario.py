d1 = {
    'str': 'valor',
    123: 'outro valor',
    (1,2,3,4): 'tupla',
    'dicionario' : 'amendoim'
}

#d1.update({'nova_chave': 'novo valor'})

#if d1.get('nomedachave') is not None:
 #   print(d1.get('str'))

#pode ser feitos de diversas maneiras por exemplo:

#for k, v in d1.items():
#print(k,v)

for k in d1.items():
    print(k)