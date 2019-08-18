'''Crie um programa que leia dois números e
mostre a soma entre eles.'''

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

soma  = num1 + num2

print("A o valor da soma é \n"
      "\033[1:34m{} + {}\033[m = {}{}" .format(num1, num2, '\033[1:36m', soma))