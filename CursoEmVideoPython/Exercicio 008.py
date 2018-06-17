'''Escreva um programa que leia um valor em
metros e o exiba convertido em centímetros e milímetros.'''

metros = float(input("Informe a medida em metros: "))

cm = metros * 100
mm = metros * 1000

print("A metragem de {} convertida em centimetros é {} cm \n"
      "e em milimetros a mesma medida é de {} mm" .format(metros,cm,mm))