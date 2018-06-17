'''Refaça o DESAFIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for'''

num = int(input("Informe um número para ver a tabuada: "))
for c in range(1,11):
    print("{} x {} = {}".format(c, num, c * num))