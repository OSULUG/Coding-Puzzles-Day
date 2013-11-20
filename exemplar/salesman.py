#! /usr/bin/env python
import re
from math import sqrt
import itertools
def get_points(filename):
    fd = open(filename)
    pts = re.sub('[\]\[]', '', fd.read()) 
    pts = pts.split('), (')
    pts = [re.sub('[\n\(\)]', '', p) for p in pts]
    pts = [p.split(', ') for p in pts]
    pts = [[int(q) for q in p] for p in pts]
    fd.close()
    return pts   

def length(x, y):
    return sqrt( (x[0] - y[0])**2 + (x[1] - y[1])**2 )

def solve_tsp_dynamic(points):
    # Dynamic TSP from http://www.digitalmihailo.com/traveling-salesman-problem-dynamic-algorithm-implementation-in-python/
    #calc all lengths
    all_distances = [[length(x,y) for y in points] for x in points]
    #initial value - just distance from 0 to every other point + keep the track of edges
    A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
    cnt = len(points)
    for m in range(2, cnt):
        B = {}
        for S in [frozenset(C) | {0} for C in itertools.combinations(range(1, cnt), m)]:
            for j in S - {0}:
                B[(S, j)] = min( [(A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j]) #this will use 0th index of tuple for ordering, the same as if key=itemgetter(0) used
        A = B
    res = min([(A[d][0] + all_distances[0][d[1]], A[d][1]) for d in iter(A)])
    return res[1]

def main():
    points = get_points('../inputs/salesman_in')
    result = solve_tsp_dynamic(points)
    f_out = open('salesman_out', 'w')
    for r in result:
        pair = points[r]
        f_out.write(str(pair) + '\n')
    f_out.close()

main()
