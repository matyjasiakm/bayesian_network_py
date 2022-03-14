__author__ = "Mateusz Matyjasiak"

import random


# Klasa węzła używana do tworzenia sieci bayesa.
# name - nazwa węzła musi być zgodna z nazwą znajdującą się w tabeli prawdopodobieństw
# prop_table - tablica prawdopodobieństw kolumny z nazwami odpowiadają warunkom, natomiast kolumna 0 odpowiada że węzeł może przyjąć zero, a 1, że jeden
# parents_list_instances = lista węzłów, które są rodzicami danego węzła.
class Node:
    def __init__(self, name, prop_table, parents_list_instances=[]):
        self.name = name
        self.prop_table = prop_table
        self.parents = parents_list_instances
        self.zero_or_one = None


# Klasa przechowująca węzły sieci Node oraz modelująca sieć bayesa.
class BayesianNetwork:
    def __init__(self):
        self.nodes_list = []

    # Dodaje węzeł node do sieci
    def add_node(self, node):
        self.nodes_list.append(node)

    # Inicializuje losowo stany początkowe węzłów
    def __init_start_nodes_state(self):
        for node in self.nodes_list:
            node.zero_or_one = random.choices([0, 1])[0]

    # Zwraca węzły dzieci podanego węzła.
    def __get_node_children(self, parent_node):
        childrens = []
        for node in self.nodes_list:
            if parent_node in node.parents:
                childrens.append(node)
        return childrens

    # Funkcja oblicza prawdopodobieństwa z otoczki markowa węzła node i losuje z tym prawdopodobieństwem wartość węzła node i jemu przypisuje.
    def __get_condi_propability_for_node(self, node):
        df_copy = node.prop_table.copy()
        prop_for_0 = 1.0
        prop_for_1 = 1.0
        #Prawdopodobieństwo warunkowe dla rodziców
        for parent in node.parents:
            df_copy = df_copy[df_copy[parent.name] == parent.zero_or_one]
        prop_for_0 *= df_copy.iloc[0]['0']
        prop_for_1 *= df_copy.iloc[0]['1']
        if node.parents.__len__ == 0:
            prop_for_0 *= df_copy.iloc[0]['0']
            prop_for_1 *= df_copy.iloc[0]['1']
        childrens = self.__get_node_children(node)
        # Prawdopodobieństwo warunkowe w dzieciach
        for child in childrens:
            df_copy = child.prop_table.copy()
            for child_parent in child.parents:
                df_copy = df_copy[df_copy[child_parent.name] == child_parent.zero_or_one]
            prop_for_0 *= df_copy.iloc[0]['0']
            prop_for_1 *= df_copy.iloc[0]['1']
        return prop_for_0 * (1 / (prop_for_1 + prop_for_0)), prop_for_1 * (1 / (prop_for_1 + prop_for_0))

    # Funkcja generuje zbiór danych liczności draw, każda instancja jest tworzona przez t iteracji.
    def sample(self, draws_number, t):
        draws = []
        for _ in range(draws_number):
            self.__init_start_nodes_state()
            for _ in range(t):
                node = random.choice(self.nodes_list)
                weights = self.__get_condi_propability_for_node(node)
                new_val = random.choices([0, 1], weights, k=1)[0]
                node.zero_or_one = new_val
            draw = []
            for node in self.nodes_list:
                draw.append((node.name, node.zero_or_one))
            draws.append(draw)
        return draws


def print2(sample):
    for samp in sample:
        print(samp)
