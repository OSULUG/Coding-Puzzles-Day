#! /usr/bin/env python
import string
from collections import defaultdict
import re
import itertools 

"""
Using the given dictionary ('words'), find all sets of n words which are all
anagrams of each other. n is given in the file ../inputs/anagram_in
"""
def get_dictionary():
    fd = open('../inputs/words', 'r')
    words = []
    for l in fd.readlines():
        words.append(re.sub('\n', '', l.lower()))
    return words

def is_anagram(a, b):
    if len(b) != len(a):
        return False
    asrt = sorted(a)
    bsrt = sorted(b)
    for i in range(0, len(a)):
        if asrt[i] != bsrt[i]:
            return False
    return True


def main():
    words = get_dictionary()
    found = []
    l = len(words)
    for i in range(l):
        print i
        finds = []
        for j in range(i+1, l):
            if is_anagram(words[i], words[j]):
                print "found"
                finds.append(words[j])
        if len(finds) > 0:
            finds.append(words[i])
            found.append(finds)
    print found
    fd = open('anagram_out', 'w')
    found.sort(key=len)
    found.reverse()
    fd.write(str(len(found[0])))
    fd.close()

main()
