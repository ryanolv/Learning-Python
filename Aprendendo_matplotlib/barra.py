"""
Aluno: Ryan da Silva Oliveira
Turma: 15
Programação Imperativa
"""

import csv
from matplotlib import pyplot as plt


def transforma(lst):
    return [int(x) for x in lst]


plt.style.use('ggplot')

with open('wealth-per-country.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    countries = []
    median_wealth = []
    mean_wealth = []
    population = []

    for line in csv_reader:
        countries.append(line['Country'])
        median_wealth.append(line['Median_Wealth'].replace(',', ''))
        mean_wealth.append(line['Mean_Wealth'].replace(',', ''))
        population.append(line['Population'].replace(',', ''))

median_wealth = transforma(median_wealth)
mean_wealth = transforma(mean_wealth)
population = transforma(population)

largura = 0.15
plt.bar(countries, median_wealth, color='yellowgreen', width=-largura - 0.04, label='Median_Wealth', align='edge')
plt.bar(countries, population, color='mediumturquoise', width=largura + 0.045, label='Population', align='edge')
plt.bar(countries, mean_wealth, color='#e5ae38', width=largura, label='Mean_Wealth', align='center')

plt.title('Dados sobre Países (Milhões)')
plt.xlabel('Países')
plt.ylabel('Dados (em milhoões)')

plt.legend()
plt.show()
