# -*- coding: utf-8 -*-
"""2_lab_networks.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-fSTeUwg8gXbvsKzzZGt8H63EbM6mUB8
"""

# Требуется получить центральность для восьми узлов «горкой», т.е. с ростом в центре списка значений и опусканием на краях.
import networkx as nx

# Создание графа с 8 узлами
G = nx.path_graph(8)

# Вычисление центральности
centrality = nx.eigenvector_centrality(G, max_iter=200)

# Вывод центральностей
print("Центральности узлов (горка):")
for node, value in sorted(centrality.items()):
    print(f"Узел {node}: Центральность {value:.4f}")

import matplotlib.pyplot as plt

# Визуализация графа
plt.figure(figsize=(8, 4))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, edge_color='gray')
plt.title("Граф с 8 узлами (линейный граф)", fontsize=14)
plt.show()

# В результате была создана сеть в виде простого пути из 8 узлов, соединенных последовательно
# Максимальные значения центральности у узлов 3 и 4
