import matplotlib.pyplot as plt
import csv

def tratarDadoAux():
    with open('athlete_events.csv') as arq:
        reader = csv.DictReader(arq)
        for row in reader:
             yield row["Games"]

def validarDado(dado):
    jogos = set(tratarDadoAux())
    if dado not in jogos:
        print('Arquivo nao encontrado.\n'
              'Veja se digitou corretamente.')
        quit()


def numero_jogadores_esporte(lst, qtd):
    conts = {}
    for i in lst:
        conts[i] = conts.get(i, 0) + 1

    esportes = []
    for k, v in conts.items():
        esportes.append((v, k))
    esportes.sort(reverse=True)
    return dict(esportes[:qtd])


def filtra_criterios(arq, criterio1):
    lst = []
    for line in arq:
        if line["Games"] == criterio1:
            lst.append(line["Sport"])
    return lst


def gerarGraficoBar(eixos):
    plt.bar(eixos[0], eixos[1], color='green')
    plt.ylabel('Número de Jogadores')
    plt.xlabel('Esportes')
    plt.title('Numero de jogadores por esportes na olimpíada de <Ano> de <Tipo de Olimpíada> ')
    plt.show()


def gerarDados(ano_tipo, quantidade_esportes):
    with open('athlete_events.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        esportes = filtra_criterios(csv_reader, ano_tipo)
        xy = numero_jogadores_esporte(esportes, quantidade_esportes)
        eixo_y = xy.keys()
        eixo_x = xy.values()
        return (eixo_x, eixo_y)


def apresentarGraficoBar(ano_tipo, quantidade_esportes):
    gerarGraficoBar(gerarDados(ano_tipo, quantidade_esportes))
