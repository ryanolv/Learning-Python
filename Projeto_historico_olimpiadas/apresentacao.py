import graficoBar as barra
import linha
import boxplot
import resp_text
import extra


def introducao():
    with open('textos.txt') as texto:
        text = texto.read()
        print(text)


def menu():
    opc = int(input('\nSua opção: '))

    if opc == 0:
        print("\nAte logo.")
        exit()

    if opc == 1:
        genero = input("Digite qual genero voce quer: ")
        linha.validarDado(genero)
        linha.apresentarGraficoLinha(genero)
        exit()

    if opc == 2:
        ano_tipo = input("Digite o ano e o tipo de Olimpiada: ")
        barra.validarDado(ano_tipo)

        quantidade_esportes = int(input("Digite a quantidade de esportes: "))
        barra.apresentarGraficoBar(ano_tipo, quantidade_esportes)
        exit()

    if opc == 3:
        genero = input("Digite qual genero voce quer: ")
        boxplot.validarDado(genero)
        boxplot.apresentarGraficoBox(genero)
        exit()

    if opc == 4:
        resp_text.apresentarRespTextual()
        exit()

    if opc == 5:
        anos = input("Digite o periodo que deseja: ").split()
        tipo_evento = input("Qual a estacao deseja? 'Winter' ou 'Summer'\n")
        extra.validarDados(tipo_evento)
        extra.apresentarGrafico(anos, tipo_evento)
        exit()
