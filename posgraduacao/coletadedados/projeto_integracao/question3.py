#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import pygraphviz as pgv

G = pgv.AGraph(directed=True)

G.node_attr['style']='filled'
G.node_attr['shape']='circle'
G.node_attr['fontcolor']='#000000'

G.graph_attr['label'] = 'Grafo de avaliação da relação entre a escolaridade dos pais com a notas do inscritos no ENEM 2011'

G.add_edge('ENEM 2011', 'Inscritos em que os \npais não estudaram', label='composto')
G.add_edge('ENEM 2011', 'Inscritos em que os \npais estudaram \no ensino médio(completo)', label='composto')
G.add_edge('ENEM 2011', 'Inscritos em que os \npais estudaram \no ensino superior(completo)', label='composto')

G.add_edge('Inscritos em que os \npais não estudaram', '466.3391', label='média', fillcolor='red')
G.add_edge('Inscritos em que os \npais estudaram \no ensino médio(completo)', '525.0187', label='média', fillcolor='red')
G.add_edge('Inscritos em que os \npais estudaram \no ensino superior(completo)', '576.0429', label='média', fillcolor='green')

print(G.string()) # print to screen
print("Wrote question3.dot")
G.write('question3.dot') # write to simple.dot

B = pgv.AGraph('question3.dot') # create a new graph from file
B.layout() # layout with default (neato)
B.draw('question3.png', prog="dot") # draw png
print("Wrote question3.png")
