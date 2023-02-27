                    #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 복수의 빈도 파일을 병합하는 프로그램

import sys
import heapq

###############################################################################
def merge_k_sorted_freq(input_files):
    '''
    input_files : list of input filenames (frequency files; 2 column format)
    '''
    fins = []
    k = len(input_files)
    heap = []
    finished = [False for _ in range(k)] # [False] * k
    
    for i in input_files:
        fins.append(open(i))

    for i in range(k):
        a=fins[i].readline()
        b=a.rstrip().split('\t')
        if len(b)<2:
            continue
        b.append(i)
        heapq.heappush(heap,b)
    
    tmp=[heap[0][0],0]
    while len(heap):
        c=heapq.heappop(heap)
        c[1]=int(c[1])
        if c[0]==tmp[0]:
            tmp[1]+=c[1]
        else:
            print(tmp[0],tmp[1],sep='\t')
            tmp=c
        d=fins[c[2]].readline().rstrip()
        if d:
            b=d.split('\t')
            if len(b)<2:
                continue
            b.append(c[2])
            heapq.heappush(heap,b)
        else:
            finished[c[2]]=True
    print(tmp[0],tmp[1],sep='\t')
            

    
    
    for i in range(k):
        fins[i].close()

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    merge_k_sorted_freq( sys.argv[1:])
