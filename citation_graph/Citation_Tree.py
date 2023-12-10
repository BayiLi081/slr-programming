import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random

def sort_dict(data_papers,column_i):
    # this function will sort the papers by years
    #x[1] refers to value of x, while x[0] is the key.
    data_papers_sorted_list=sorted(data_papers.items(), key=lambda x: x[1][column_i])

    # convert the list back into the dictionary
    data_papers_sorted={}
    for paper in data_papers_sorted_list:
        data_papers_sorted[paper[0]]=paper[1]

    return data_papers_sorted

##### Section: remove non selected children; create data frame #####

# sort papers by years; 1 means the "2nd column" of one_paper_data
data_all_papers=sort_dict(data_all_papers,1)

bibCode_all_papers=list(data_all_papers.keys())

from_all_papers=[]
to_all_papers=[]
for bibCode_one_paper, data_one_paper in data_all_papers.items():
    list_children=data_one_paper[-1]
    list_children_remained=[x for x in list_children if x in bibCode_all_papers]
    data_one_paper[-1]=list_children_remained
    data_all_papers[bibCode_one_paper]=data_one_paper

    # create data frame
    num_child=len(list_children_remained)

    vrt_name_children_remained=[]
    for bibCode_child_i in list_children_remained:
        vrt_name_multi_lines=data_all_papers[bibCode_child_i][-2]
        vrt_name_children_remained.append(vrt_name_multi_lines)

    vrt_name_one_paper=data_all_papers[bibCode_one_paper][-2]

    from_one_paper=vrt_name_children_remained # the older paper
    to_one_paper=[vrt_name_one_paper]*num_child # the newer paper

    # concatenate the lists
    from_all_papers=from_all_papers+from_one_paper
    to_all_papers=to_all_papers+to_one_paper

##### Section: Draw Graph #####

# Build a dataframe with 4 connections
df = pd.DataFrame({ 'from':from_all_papers, 'to':to_all_papers})

# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())

# determine vertices' coordinate
if not nx.is_directed_acyclic_graph(G):
    raise TypeError('Cannot to a graph that is not a DAG')

vertices_sorted=list(nx.topological_sort(G))

num_vertices=len(vertices_sorted)

posi={}
for i in range(num_vertices):
    vrt_name=vertices_sorted[i]
    posi_vert=-i/num_vertices
    posi_hori=random.random()
    posi[vrt_name]=np.array([posi_hori,posi_vert])

# make the vertices less dense
posi_new = vertices_less_dense(posi)

# logic similar to the EM algorithm to get a "good graph"
for i in range(round(num_vertices*1.4)):
    posi_new = vertices_less_dense(posi_new)

# if the graph doesn't look good, change figsize and rerun the last 3 lines
plt.figure(1,figsize=(18,18))
nx.draw(G,pos=posi_new,with_labels=True, node_size=150, arrows=True)
plt.show()
