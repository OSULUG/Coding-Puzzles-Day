#! /usr/bin/env python
import re # regular expression library
"""
Your task is to write a function which traverses the list and finds the
smallest value in it. Hint: def myTraversal(list):
"""
class Link:
    def __init__(self, data, n = None):
        self.d = data
        self.n = n
    def show(self):
        return str(self.d)

class LinkList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newLink = Link(data, self.head)
        self.head = newLink
    def stringTraverse(self):
        l = self.head
        output = ''
        while l is not None:
            output = output + l.show() + ' '
            l = l.n
        return output + '\n'
    def min(self):
        l = self.head
        l_min = l.d
        while l is not None:
            if (l.d < l_min):
                l_min = l.d
            l = l.n
        return l_min
            
            

def makeList():
    fd = open('linklist_in','r')
    l = fd.read()
    fd.close()
    elements = re.sub('[\[\],\n]','', l).split()
    l = LinkList()
    for e in elements:
        l.append(e)
    return l

def writeToOutput(mystring):
    fd = open('linklist_out', 'w')
    fd.write(mystring) # final solution should actually write the smallest
                       # number from the linked list 
    fd.close()


def main():
    mylist = makeList()
    writeToOutput(mylist.stringTraverse())
    writeToOutput(str(mylist.min()))
main()
