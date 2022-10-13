
"""
Formatando valores
:s - texto(strings)
:d- inteiros(int)
:f- pontos flutuantes(float)
:.(número)f- quantidade de casas decimais(float)
:(Char)(> or < or ^)(Quantidade)(type- s,d ou f)
>- Left
<- right
^- Center
"""
n1=10
n2=3
div= n1/n2

print('{:.2f}'.format(div))
"""or"""
print(f'{div}')