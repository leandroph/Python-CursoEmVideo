'''Faça um programa que leia um número
Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

num = int(input("Digite um número inteiro: "))

print("O antessor de {} é {}\n"
      "O sucessor de {} é {}" .format(num, num-1, num, num+1))