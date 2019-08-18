'''Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

catOposto = float(input("Informe o valor do cateto oposto"))
catAjacente = float(input("Informe o valor do cateto oposto"))

hipotenusa = hypot(catOposto, catAjacente)

print("O comprimento da hipotenusa é {:.2f}".format(hipotenusa))
