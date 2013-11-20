#! /usr/bin/env python
import re
f_in = open('../inputs/subsets_in', 'r')
f_out = open('subsets_out', 'w')

l = re.sub('[\]\[,]', '', f_in.read())
l = [int(v) for v in l.split()]

def search(l):
    count = 0
    ixs = range(len(l))
    subsets = []
    for i in xrange(2 ** len(l)):
        subset = [l[ix] for ix in ixs if i & (1 << ix)]
        if sum(subset) == 0:
            subsets.append(subset)
            print subset
            # f_out.write(str(subset) + '\n')
    f_out.write(str(len(list(set(map(tuple, subsets))))) + '\n')
search(l)
f_in.close()
f_out.close()

