'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

print("##### CONVERSOR DE TIPOS #####")
print("CONVERSOR")

numero = int(input("Digite um número para realizar a conversão: "))
tipo = int(input("1 - PARA BINÁRIO\n"
      "2 - PARA OCTAL\n"
      "3 - PARA HEXADECIMAL"))

if (tipo == 1):
    print("O número {} convertido para BINÁRIO é {}".format(numero, bin(numero)[2:]))
elif (tipo == 2):
    print("O número {} convertido para OCTAL é {}".format(numero, oct(numero)[2:]))
elif (tipo == 3):
    print("O número {} convertido para HEXADECIMAL é {}".format(numero, hex(numero)[2:]))
else:
    print("Tipo selecionado inválido!!")