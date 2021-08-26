import csv
from matplotlib import pyplot as plt


def validarDados(str):
    if str != 'Summer' and str != 'Winter':
        print("Arquivo nao encontrado.")
        exit()


def fil_jog_sex_ano(list_dict, ano_i, ano_f, evento, sex):
    jog = filter(lambda p: p["Year"] >= ano_i and p["Year"] <= ano_f
                           and p["Sex"] == sex and p["Season"] == evento
                           and p["Height"] != 'NA' and p["Weight"] != 'NA', list_dict)

    return list(jog)


def calcula_imc(list_dict):
    jogos = {}
    media_imc = {}
    # Ordena eixo x do grafico
    list_dict.sort(key=lambda p: p["Year"])

    for p in list_dict:
        peso, altura, ano = float(p["Weight"]), float(p["Height"])/100, p["Year"]
        imc = peso / (altura * altura)
        jogos[ano] = jogos.get(ano, 0) + 1
        media_imc[ano] = media_imc.get(ano, 0) + imc

    # Calcula a media de imc a cada ano
    for p in media_imc:
        media_imc[p] /= jogos[p]

    return media_imc


def gerarDados(anos, evento, sex):
    with open('athlete_events.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        ano1, ano2 = anos[0], anos[1]
        jogadores = fil_jog_sex_ano(csv_reader, ano1, ano2, evento, sex)
        ano_media = calcula_imc(jogadores)

        return ano_media


def gerarEixos(man, woman):
    ei_x = man.keys()
    y_mas = man.values()
    y_fem = woman.values()

    return ei_x, y_mas, y_fem


def gerarGrafico(anos, evento):
    y_masculino = gerarDados(anos, evento, 'M')
    y_feminino = gerarDados(anos, evento, 'F')
    ei_x, y_mas, y_fem = gerarEixos(y_masculino, y_feminino)

    plt.plot(ei_x, y_mas, color='darkslateblue', marker='o', linewidth=3, label='Masculino')
    plt.plot(ei_x, y_fem, color='blueviolet', marker='*', linewidth=3, label='Feminino')
    plt.xticks(rotation=45)
    plt.xlabel("Edicoes dos jogos ")
    plt.ylabel("Media de IMC")
    plt.title("Evolucao da media de IMC a cada ano")
    plt.legend()
    plt.show()


def apresentarGrafico(anos, tipo_evento):
    gerarGrafico(anos, tipo_evento)
