__author__ = "Mateusz Matyjasiak"
from collections import Counter

import pandas as pd

from bayes_Mateusz_Matyjasiak import Node, BayesianNetwork, print2


# Funkcja przekształca wynik na liczbę binarną
def to_binary_string_vector_list(sample):
    result = []
    for samp in sample:
        vector = ''
        for row in samp:
            vector += str(row[1])
        result.append(vector)
    return result


# Prawdopodobieństwa
zima = {'0': [0.75],
        '1': [0.25]}
szczyt = {'0': [0.25],
          '1': [0.75]}

korek = {'Szczyt': [0, 1],
         '0': [0.8, 0.15],
         '1': [0.2, 0.85]}
zla_pogoda = {'Zima': [0, 1],
              '0': [0.33, 0.15],
              '1': [0.67, 0.85]}
wypadek = {'Zla_Pogoda': [0, 1, 0, 1],
           'Korek': [0, 1, 1, 0],
           '0': [0.90, 0.01, 0.45, 0.40],
           '1': [0.1, 0.99, 0.55, 0.6]}
zima_df = pd.DataFrame(zima)
szczyt_df = pd.DataFrame(szczyt)
korek_df = pd.DataFrame(korek)
zla_pogoda_df = pd.DataFrame(zla_pogoda)
wypadek_df = pd.DataFrame(wypadek)

zima_node = Node('Zima', zima_df)
szczyt_node = Node('Szczyt', szczyt_df)
korek_node = Node('Korek', korek_df, [szczyt_node])
zla_pogoda_node = Node('Zla_Pogoda', zla_pogoda_df, [zima_node])
wypadek_node = Node('Wypadek', wypadek_df, [korek_node, zla_pogoda_node])

network = BayesianNetwork()
network.add_node(zima_node)
network.add_node(szczyt_node)
network.add_node(korek_node)
network.add_node(zla_pogoda_node)
network.add_node(wypadek_node)

draws = network.sample(10000, 100)
print2(draws)

draws_flat = to_binary_string_vector_list(draws)

print2(draws_flat)
draws_flat.sort()
print(Counter(draws_flat).keys())
print(Counter(draws_flat).values())
