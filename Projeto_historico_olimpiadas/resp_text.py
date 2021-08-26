import csv


def achar_maior(dict):
    maior_valor = 0
    ano = None

    for year in dict:
        if dict[year] > maior_valor:
            maior_valor = dict[year]
            ano = year

    return ano


def count_partic(list_dict):
    count = {}

    for dados in list_dict:
        count[dados["Year"]] = count.get(dados["Year"], 0) + 1

    return achar_maior(count)


def count_sexo(list_dict, digito):
    atletas_ano = filter(lambda p: p["Year"] == digito, list_dict)
    count = {}

    for dados in atletas_ano:
        count[dados["Sex"]] = count.get(dados["Sex"], 0) + 1

    if count['M'] > count['F']:
        return 'Masculino'
    else:
        return 'Feminino'


def tratarDados():
    with open('athlete_events.csv') as csv_file:
        csv_Reader = csv.DictReader(csv_file)
        csv_Reader = list(csv_Reader)

        ano_maior_partic = count_partic(csv_Reader)
        sexo_maioria = count_sexo(csv_Reader, ano_maior_partic)

        return ano_maior_partic, sexo_maioria


def formatarResposta():
    ano, sexo = tratarDados()
    print(f'\nO ano com maior participacao de atletas foi {ano}, com maioria de sexo {sexo}')


def apresentarRespTextual():
    formatarResposta()
