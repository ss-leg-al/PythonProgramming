#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import get_morphs_tags as mf

###############################################################################
# 색인어 추출
def get_index_terms( mt_list):
    nouns = []
    indexterms=('NNG','NNP','SL','SN','SH')
    s=''
    count=0
    for i in range(len(mt_list)):
        if mt_list[i][1] in indexterms:
            nouns.append(mt_list[i][0])
            count+=1
            s+=mt_list[i][0]
            if i==(len(mt_list)-1) and count>1:
                nouns.append(s)
        else:
            if count>1:
                nouns.append(s)
            s=''
            count=0
        
    return nouns

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open( sys.argv[1]) as fin:

        mt_freq = {}
    
        # 2 column format
        for line in fin.readlines():

            segments = line.split('\t')

            if len(segments) < 2:
                continue

            # 형태소, 품사 추출
            # result : list of tuples
            result = mf.get_morphs_tags(segments[1].rstrip())
    
            # 색인어 추출 (명사 및 복합명사 등)
            terms = get_index_terms( result)
        
            # 색인어 출력
            for term in terms:
                print(term)
