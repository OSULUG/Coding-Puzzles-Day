#! /usr/bin/env python
import re
f_in = open('../samples/subsets_in', 'r')
f_out = open('subsets_out', 'w')

l = re.sub('[\]\[,]', '', f_in.read())
l = [int(v) for v in l.split()]

def search(l):
    sum = 0
    ixs = range(l[:-1])
    for i in xrange(2 * len(l)):
        subset = [l[ix] for ix in ix if i & (1 << ix)]
        if sum(subset) == 0:
            sum += 1
            f_out.write(str(subset) + '\n')
    return sum
f_out.write(search(l))
close(f_in)
close(f_out)

