'''Crie um programa que leia um número Real qualquer pelo
teclado e mostre na tela a sua porção Inteira.'''
import math
num = float(input("Digite um valor real"))

print("O valor digitado foi {} e seu valor inteiro é {}".format(num, math.trunc(num)))