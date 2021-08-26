from matplotlib import pyplot as plt
import csv

def validarDado(dado):
    if dado != 'M' and dado != 'F':
        print('\nDado nao encontrado.\nTente ver se nao digitou errado')
        exit()


def filt_atletas_gen_ouro(genero, arq):
    # Filtrado os atletas do genero que levaram ouro e idade sem NA
    atletas = filter(lambda p: p["Sex"] == genero and p["Medal"] == 'Gold'
                     and p["Age"] != 'NA', arq)
    return list(atletas)


def dict_jogo_idade(list_dict):
    jogo_quant_jogador = {}
    jogo_idade = {}

    # Ordena eixo x do grafico
    list_dict.sort(key=lambda p: p["Year"])

    for p in list_dict:
        jogo_quant_jogador[p["Year"]] = jogo_quant_jogador.get(p["Year"], 0) + 1
        jogo_idade[p["Year"]] = jogo_idade.get(p["Year"], 0) + int(p["Age"])

    # Calcula a media das idades a cada ano
    for p in jogo_idade:
        jogo_idade[p] /= jogo_quant_jogador[p]

    return jogo_idade


def gerar_eixox_eixoy(dict):
    list_edicoes = []
    list_media_idade = []

    for edicao, media_idade in dict.items():
        list_edicoes.append(edicao)
        list_media_idade.append(media_idade)

    return (list_edicoes, list_media_idade)


def gerarDados(genero):
    with open('athlete_events.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        atletas = filt_atletas_gen_ouro(genero, csv_reader)
        jogo_media_idade = dict_jogo_idade(atletas)

        return gerar_eixox_eixoy(jogo_media_idade)


def gerarGrafico(genero):
    x, y = gerarDados(genero)
    plt.plot(x, y, color='#444444', marker='*')
    plt.xlabel("Edicoes da Olimpiada")
    plt.ylabel("Evolucao da Idade Media ")
    plt.xticks(rotation=45)
    plt.title(f"Evolucao da idade media dos atletas do genero {genero} que ganharam medalha de ouro \
em alguma das Olimpiadas.")
    plt.grid(True)
    plt.show()

def apresentarGraficoLinha(genero):
    gerarGrafico(genero)

