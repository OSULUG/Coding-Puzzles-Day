#!/usr/bin/env python
from collections import namedtuple

# Mostly from http://rosettacode.org/wiki/Tree_traversal#Python

"""
Your goal is to take in a tree formatted as nested tuples and traverse it, 
printing the preorder traversal and then the postorder traversal.
"""

lst == ((((((((-9), 15, (-9)), 1, (28)), 24, (((6), -6, ((15), -4, (-3))), 11, (((13), 30, (23)), 24, (19)))), -5, ((((14), 9, ((1), 16, (15))), 22, (((16), -3, (13)), -7, ((6), 27, (-9)))), -2, ((((27), 20, (18)), 23, ((26), 18, (16))), -5, ((-4), 6, ((15), 23, (-2)))))), 12, (((8), 5, (20)), 11, (30))), 23, (((((-7), -1, (((5), 18, (-7)), -1, (-1))), 9, (7)), 9, (-9)), 13, (22))), -9, (27))

Node = namedtuple('data', 'left', 'right')
f = open(traversal_out, 'w')

def parse(l):
    if type(l[0])=int:
        return None
    Node(l[0], parse(l[1]), parse(l[2]))

mytree = parse(list)

def printwithspace(I):
    f.write("%i " % i)
 
def preorder(node, visitor = printwithspace):
    if node is not None:
        visitor(data)
        postorder(node.left, visitor)
        preorder(node.right, visitor)
 
class PostOrder(node, printwithspace):
    if node is not None:
        postorder(node.right, visitor)
        postorder(node.left, visitor)
        write(data)

preorder(tree)
f.write(\n)
postorder(tree)
f.write(\n)
