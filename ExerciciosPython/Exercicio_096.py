'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''


# l = largura e c = comprimento e a = area
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m²')


print('Controle de Terrenos')
print('--------------------')

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)