#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

###############################################################################
def word_count(filename):
    """ 단어 빈도 dictionary를 생성한다. (key: word, value: frequency)
    
    filename: input file
    return value: a sorted list of tuple (word, frequency) 
    """
    f=open(filename)
    d={}
    for a in f.readlines():
        a=a.strip()
        if a in d.keys():
            d[a]+=1
        else:
            d[a]=1
    r=list(d.items())
    r.sort(key=lambda x:x[0])
    return r




















###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    result = word_count( sys.argv[1])

    # list of tuples
    for w, freq in result:
        print( "%s\t%d" %(w, freq))
