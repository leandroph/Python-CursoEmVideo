'''Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''

times = ('Flamengo', 'Atlético', 'São Paulo', 'Internacional', 'Grêmio',
        'Palmeiras', 'Sport Recife', 'Cruzeiro', 'Botafogo',
        'Vasco da Gama', 'Fluminense', 'América-MG', 'Chapecoense',
        'Santos', 'EC Vitória', 'Bahia', 'Paraná', 'Atlético-PR', 'Ceará SC')

print(20*'--' + "\n      CAMPEONATO BRASILEIRO 2018\n" + 20*'--')

print("Os vintes times do campeonato são {}".format(times))
print("Os cinco primeiros times da Tabela são {}".format(times[0:5]))
print(20*'--')
print("Os quatro últimos times da Tabela são {}".format(times[-4:]))
print(20*'--')
print("Os times em ordem alfabetica {}".format(sorted(times)))
print(20*'--')

for pos, time in enumerate(times):
    if time == "Chapecoense":
        print("O time do {} esta na {} posição ".format(time, pos + 1))