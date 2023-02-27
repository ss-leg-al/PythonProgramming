#!/usr/bin/env python3
# coding: utf-8

import sys

def get_morphs_tags(tagged):
    result=[]
    count=0
    a=tagged.split('+')
    for i in a:
        if len(i)==0:
            a.remove('')
            a[count]='+'+a[count]
        count+=1
    for i in a:
        d=i.split('/')
        if len(d[0])==0:
            del d[0]
            del d[0]
            d.insert(0,'/')
        result.append(tuple(d))
    return result

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1]) as fin:

        for line in fin.readlines():

            # 2 column format
            segments = line.split('\t')

            if len(segments) < 2: 
                continue

            # result : list of tuples
            result = get_morphs_tags(segments[1].rstrip())
        
            for morph, tag in result:
                print(morph, tag, sep='\t')
