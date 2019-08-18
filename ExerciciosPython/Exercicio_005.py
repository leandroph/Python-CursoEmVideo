'''Faça um programa que leia um número
Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

num = int(input("Digite um número: "))

print("O antecessor de {} é {}".format(num, num - 1))
print("O sucessor de {} é {}".format(num, num + 1))