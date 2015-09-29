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

G.graph_attr['label'] = 'Grafo de avaliação das áreas de conhecimento ENEM 2011'

G.add_edge('Área do Conhecimento', 'Ciências Humanas', label='composto')
G.add_edge('Área do Conhecimento', 'Ciências da Natureza', label='composto')
G.add_edge('Área do Conhecimento', 'Linguagens e Códigos', label='composto')
G.add_edge('Área do Conhecimento', 'Matemática', label='composto')
G.add_edge('Área do Conhecimento', 'Redação', label='composto')

G.add_edge('Ciências Humanas', '469,9806', label='média', fillcolor='red')
G.add_edge('Ciências da Natureza', '481,8640', label='média')
G.add_edge('Linguagens e Códigos', '524,7821', label='média')
G.add_edge('Matemática', '521,4110', label='média')
G.add_edge('Redação', '545,2016', label='média', fillcolor='green')

print(G.string()) # print to screen
print("Wrote question1.dot")
G.write('simple.dot') # write to simple.dot

B=pgv.AGraph('simple.dot') # create a new graph from file
B.layout() # layout with default (neato)
B.draw('question1.png', prog="dot") # draw png
print("Wrote question1.png")
