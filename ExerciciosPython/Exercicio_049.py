'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for
'''

print("##### TABUADA #####")
num = int(input("Digite um número: "))

for cont in range(1, 11):
    #:2 - vai deixar o número formato em duas casas decimais.
    print("{} x {:2} = {}".format(num, cont, cont * num))
print("ACABOU")