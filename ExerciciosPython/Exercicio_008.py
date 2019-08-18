'''Escreva um programa que leia um valor em
metros e o exiba convertido em centímetros e milímetros.'''

metros = int(input("Informe um valor em metros: "))

cm = metros * 100
mm = metros * 1000

print("A medida de {} m equivale a {} cm e {} mm".format(metros, cm, mm))