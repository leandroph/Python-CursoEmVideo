'''Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.'''

num = int(input("Informe um valor inteiro: "))

dobro = num * 2
triplo = num * 3
raizQ = num ** (1/2)#** é exponenciação

print("O número informado foi {} e seu  "
      "dobro é {}, o triplo é {} "
      "e a raiz quadrada é {:.2f}" .format(num, dobro, triplo, raizQ))
