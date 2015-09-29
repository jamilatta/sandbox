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

G.graph_attr['label'] = 'Grafo de avaliação do ensino público e privado ENEM 2011'

G.add_edge('ENEM 2011', 'Ensino Público', label='composto')
G.add_edge('ENEM 2011', 'Ensino Privado', label='composto')

G.add_edge('Ensino Público', '492.8093', label='média', fillcolor='red')
G.add_edge('Ensino Privado', '579.8989', label='média', fillcolor='green')

print(G.string()) # print to screen
print("Wrote question2.dot")
G.write('question2.dot') # write to simple.dot

B = pgv.AGraph('question2.dot') # create a new graph from file
B.layout() # layout with default (neato)
B.draw('question2.png', prog="dot") # draw png
print("Wrote question2.png")
