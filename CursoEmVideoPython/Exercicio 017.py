'''Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre o
comprimento da hipotenusa.'''
from math import hypot

catetoOp = float(input("Digite o valor do cateto oposto"))
catetoAdj = float(input("Digite o valor do cateto adjacente"))

hipotenusa = hypot(catetoOp,catetoAdj)
print("O valor da hipotenusa é {}".format(hipotenusa))