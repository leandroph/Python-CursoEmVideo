'''Faça um programa que leia algo pelo teclado e mostre na
tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

dado = input("informe algo: ")
print("É decimal {}\n"
      "é um digito {}\n"
      "é um número {}\n"
      "é um Alfa {}\n"
      "é capitalizada {}".format(dado.isdecimal(),dado.isdigit(),
            dado.isnumeric(),dado.isalpha(),dado.istitle()))
