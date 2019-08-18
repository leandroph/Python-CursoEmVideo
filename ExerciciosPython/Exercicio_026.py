'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

nome = str(input('Digite seu nome: ')).strip().upper()

print('Letra A encontrada {} vezes'.format(nome.count('A')))
print('A primeira ocorrencia da letra A é encontrada na posição {}'.format(nome.find('A') + 1))#+1 pois a string começa na posição 0
print('A última ocorrencia da letra A é encontrada na posição {}'.format(nome.rfind('A') + 1))
