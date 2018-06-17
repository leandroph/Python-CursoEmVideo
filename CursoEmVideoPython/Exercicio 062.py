'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerrará quando ele disser que
quer mostrar 0 termos.'''

termo = int(input("Informe o primeiro termo da PA"))
razao = int(input("Informe a razao da PA"))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}".format(termo), end = " ")
        termo += razao
        cont += 1
    mais = int(input("\nDeseja inserir mais alguns termos"))

print("Processo finalizado com {} termos".format(cont))