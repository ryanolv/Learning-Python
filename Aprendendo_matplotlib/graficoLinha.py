"""
Aluno: Ryan da Silva Oliveira
Turma: 15
Programação Imperativa
"""

import csv
import matplotlib.pyplot as plt


def transforma(lst):
    return [int(x) for x in lst]


plt.style.use('fivethirtyeight')

with open('sample-line.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    eixo_x = []
    eixo_y = []

    for line in csv_reader:
        eixo_x.append(line['Game Number'])
        eixo_y.append(line[' "Game Length"'])

eixo_y = transforma(eixo_y)
eixo_x = transforma(eixo_x)

plt.plot(eixo_x, eixo_y, color='lightcoral',
         linewidth=3, label="Game Number")

plt.title('Game')
plt.xlabel('Game Number')
plt.ylabel('Game Length')

plt.style.use('fivethirtyeight')

plt.legend()
plt.show()
