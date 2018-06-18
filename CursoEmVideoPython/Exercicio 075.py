'''Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input("Digite um número")),
       int(input("Digite um número")),
       int(input("Digite um número")),
       int(input("Digite um número")))

print(num)
print("O número nove apareceu {}".format(num.count(9)))
if 3 in num:
    print("O numero 3 apareceu na {} posição".format(num.index(3)))
else:
    print("O número 3 não se encontra na tupla")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")

