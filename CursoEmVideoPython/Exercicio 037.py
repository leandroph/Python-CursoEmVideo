'''Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''

num = int(input("Digite um número: "))
print("Qual conversão deseja")
print("1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL")
tipo = int(input("Qual a conversão desejada: "))

if(tipo == 1):
    print("{} convertido para BINÁRIO fica {}".format(num, bin(num)[2:]))
elif(tipo == 2):
    print("{} convertido para OCTAL fica {}".format(num, oct(num)[2:]))
elif(tipo ==3):
    print("{} convertido para OCTAL fica {}".format(num, hex(num)[2:]))
else:
    print("Tipo informado inválido")