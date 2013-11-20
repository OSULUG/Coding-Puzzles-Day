#! /usr/bin/env python

from random import randint as ri

"""
Naming convention for input and output files: problem_in and
problem_out 

"""

def salesman(n):
    """
    Write code to provide a solution to the classic Traveling Salesman Problem. 
    Input is a list of points; output should be those points in the order that 
    they should be visited to form the shortest loop which visits every one 
    then returns to the start.
    """
    arr = []
    for i in range(n):
        arr.append((ri(-100, 100), ri(-100, 100)))
    return arr

def subsets(n):
    """
    Debug the code which finds all those subsets of the given set which sum to 0.
    Desired output is the number of subsets which sum to 0.
    """
    out = []
    for i in range(n):
        out.append(ri(-50,50))
    return out

def anagram(n):
    """
    Using the given dictionary ('words'), find all sets of words which are
    all anagrams of each other. The output which you print to the file is the
    size of the largest of these sets.
    """
    return n

def traversal(d):
    """
    Debug the given code to traverse the given tree, writing the preorder traversal
    and then the postorder traversal.
    """
    if ri(0, d) == 0:
        return '(' + str(ri(-9,30)) + ')'
    else:
        return '(' + traversal(d-1) + ', ' + str(ri(-9, 30)) + ', ' + traversal(d-1) + ')'
       
def linklist(n):
    """
    Complete the code which traverses the linked list and prints its smallest
    value.
    """
    l = []
    for i in range(n):
        l.append(ri(0,9))
    return l

def arrsort(n):
    """
    Debug the code which sorts an array.
    """
    arr = []
    for i in range(n):
        arr.append(ri(-20,20))
    return arr

def main():
    if True:
        puzzles = [ (salesman, 'salesman', 5), 
                    (subsets, 'subsets', 15),
                    (anagram, 'anagram', 2),
                    (traversal, 'traversal', 5), 
                    (linklist, 'linklist', 6), 
                    (arrsort, 'arrsort', 50)]
    else:
       puzzles = [ (salesman, 'salesman', 20), 
                    (subsets, 'subsets', 26),
                    (anagram, 'anagram', 2),
                    (traversal, 'traversal', 9), 
                    (linklist, 'linklist', 20), 
                    (arrsort, 'arrsort', 50)]
    path = 'samples/'
    for fnc, name, arg in puzzles:
        f = open(path + name + '_in', 'w')
        gen = str(fnc(arg)) + '\n'
        f.write(gen)
        f.close()

main()
