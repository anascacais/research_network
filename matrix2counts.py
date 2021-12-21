# built-in
from itertools import combinations
import ast

# third party
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


try:
    bigrams = pd.read_csv('bigrams.csv', index_col=0)

except:
    df = pd.read_excel('authors.xlsm', sheet_name='papers and authors')
    bigrams = pd.DataFrame(columns=['bigrams', 'counts'])

    for i in df.index.values:

        authors = list(df.columns.values[df.iloc[i,:]==1])
        authors_bigrams = combinations(authors, 2)

        for big in authors_bigrams:

            if big in list(bigrams.bigrams.values):
                bigrams.loc[bigrams['bigrams'] == big, 'counts'] = bigrams.loc[bigrams['bigrams'] == big, 'counts'] + 1
            else:
                bigrams=bigrams.append(pd.DataFrame([[big, 1]], columns=['bigrams', 'counts']), ignore_index=True)
            
            print(bigrams)



try:
    affil = pd.read_csv('affil.csv', index_col=0)

except:
    affil = pd.read_excel('authors.xlsm', sheet_name='authors and affiliations', usecols=[0,1])
    affil.to_csv("affil.csv")

# Create dictionary of edges and their weights
d = bigrams.set_index('bigrams').T.to_dict('records')[0]
print(np.unique(list(d.values()), return_counts=True))

# remove items with a single connection
del_list = []
for key in d.keys():
  if d[key] == 1:
    del_list += [key]

for key in del_list:
    del d[key]

print(np.unique(list(d.values()), return_counts=True))

# Create network plot 
G = nx.Graph()

# Create connections between nodes
for k, v in d.items():
    k = ast.literal_eval(k)
    author1 = f'{k[0].split(",")[1][0]}. {k[0].split(",")[0]}'
    author2 = f'{k[1].split(",")[1][0]}. {k[1].split(",")[0]}'
    G.add_edge(author1, author2, weight=(v * 10))


# Get node degree in a dict for node size parameter
node_size = dict(G.degree)

fig, ax = plt.subplots(figsize=(16, 12))
pos = nx.spring_layout(G, k=2)

# Reindex the dataframe to align with graph's nodes
for i in range(affil.shape[0]):
    affil.iloc[i,0] = f'{affil.iloc[i,0].split(",")[1][0]}. {affil.iloc[i,0].split(",")[0]}'

affil = affil.set_index('Authors')
affil = affil.reindex(G.nodes())
affil['Affiliation'] = pd.Categorical(affil['Affiliation'])
affil['Affiliation'].cat.codes

print(affil['Affiliation'].cat.codes)

# Plot networks
nx.draw_networkx(G, pos,
                 font_size=8,
                 width=2,
                 edge_color='grey',
                 node_color=affil['Affiliation'].cat.codes,
                 with_labels = True,
                 ax=ax,
                 cmap='viridis',
                 node_size=[v * 80 for v in node_size.values()])

import matplotlib as mpl
import matplotlib.cm as cm

cdict = affil['Affiliation'].cat.codes.to_dict()
norm = mpl.colors.Normalize(vmin=min(list(cdict.values())), vmax=max(list(cdict.values())))
m = cm.ScalarMappable(norm=norm, cmap='viridis')


legend = []
for i in range(max(list(cdict.values()))):
    a = affil.loc[list(cdict.keys())[list(cdict.values()).index(i)], 'Affiliation']
    legend += [mpatches.Patch(color=m.to_rgba(i), label=a)]

ax.legend(handles=legend)
plt.show()

print('done')