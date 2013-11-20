#! /usr/bin/env python

import sys
from os import listdir
from collections import defaultdict
from difflib import Differ

"""
Naming convention for input and output files: problem_in and
problem_out 

Each contestant places their code in a directory named after themself. 
Only the *_out files in each contestant's directory will be counted.
"""

def compare(contestant, puzzle):
    if puzzle + '_out' not in listdir('contestants/' + contestant):
        return False
    dfr = Differ()
    diff = list(dfr.compare(open('exemplar/' + puzzle + '_out').readlines(),\
          open('contestants/' + contestant + '/' + puzzle +'_out').readlines()))
    if len(diff) > 0:
        return False
    return True
def main():
    puzzles = [ ('salesman', 7),
                ('subsets', 7),
                ('anagram', 5),
                ('traversal', 5),
                ('linklist', 2),
                ('arrsort', 2)]
    scores = defaultdict(int)
    contestants = listdir('contestants')
    for c in contestants:
        for p in puzzles:
            if compare(c, p[0]):
                scores[c] += p[1]
    for c in contestants:
        print c
        print scores[c]
main()
