'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''


def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos
    :param num: uma ou mais notas dos alunos (aceita várias notas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num) / len(num)

    #só vai exibir se a situação for Verdadeira
    if sit:
        if r["média"] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


#Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)