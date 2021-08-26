from matplotlib import pyplot as plt
import csv


def validarDado(dado):
    if dado != 'M' and dado != 'F':
        print('\nDado nao encontrado.\nTente ver se nao digitou errado')
        exit()


def fil_jog_gen(dict, var):
    jogadores = filter(lambda p: p["Sex"] == var and p["Weight"] != 'NA', dict)
    return list(jogadores)


def dict_peso_jogo(list_dict):
    count = {}

    list_dict.sort(key=lambda p: p["Year"])

    for p in list_dict:
        if p["Year"] not in count:
            count[p["Year"]] = [float(p["Weight"])]
        else:
            count[p["Year"]] += [float(p["Weight"])]
    return count


def gera_eixos(dict):
    eixo_x = []
    eixo_y = []

    for k, v in dict.items():
        eixo_x.append(k)
        eixo_y.append(v)

    return (eixo_x, eixo_y)


def gerarDados(str):
    with open('athlete_events.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        jogadores = fil_jog_gen(csv_reader, str)
        games_pesos = dict_peso_jogo(jogadores)
        tupla_eixos = gera_eixos(games_pesos)

        return tupla_eixos


def geraGrafico(str):
    x, y = gerarDados(str)
    plt.boxplot(y, labels=x)
    plt.xlabel('Edicoes da Olimpiada')
    plt.ylabel('Pesos dos atletas')
    plt.xticks(rotation=45)
    plt.title('Pesos dos atletas a cada ano')
    plt.show()


def apresentarGraficoBox(str):
    geraGrafico(str)
