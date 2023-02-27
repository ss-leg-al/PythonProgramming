#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

_CHO_ = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
_cho=list(_CHO_)
_JUNG_ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
_jung=list(_JUNG_)
_JONG_ = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ' # index를 1부터 시작해야 함
_jong=list(_JONG_)
_jong.insert(0,'')

# 겹자음 : 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'
ggja=['ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ']
ggmo=['ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']
# 겹모음 : 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'
def decomposggja(a):
    if a=='ㄳ':
        return ['ㄱ','ㅅ']
    elif a=='ㄵ':
        return ['ㄴ','ㅈ']
    elif a=='ㄶ':
        return ['ㄴ','ㅎ']
    elif a=='ㄺ':
        return ['ㄹ','ㄱ']
    elif a=='ㄻ':
        return ['ㄹ','ㅁ']
    elif a=='ㄼ':
        return ['ㄹ','ㅂ']
    elif a=='ㄽ':
        return ['ㄹ','ㅅ']
    elif a=='ㄾ':
        return ['ㄹ','ㅌ']
    elif a=='ㄿ':
        return ['ㄹ','ㅍ']
    elif a=='ㅀ':
        return ['ㄹ','ㅎ']
    elif a=='ㅄ':
        return ['ㅂ','ㅅ']
    else: 
        return False

def makingggja(a,b):
    if a=='ㄱ' and b=='ㅅ':
        return 'ㄳ'
    elif a=='ㄴ' and b=='ㅈ':
        return 'ㄵ'
    elif a=='ㄴ' and b=='ㅎ':
        return 'ㄶ'
    elif a=='ㄹ' and b=='ㄱ':
        return 'ㄺ'
    elif a=='ㄹ' and b=='ㅁ':
        return 'ㄻ'
    elif a=='ㄹ' and b=='ㅂ':
        return 'ㄼ'
    elif a=='ㄹ' and b=='ㅅ':
        return 'ㄽ'
    elif a=='ㄹ' and b=='ㅌ':
        return 'ㄾ'
    elif a=='ㄹ' and b=='ㅍ':
        return 'ㄿ'
    elif a=='ㄹ' and b=='ㅎ':
        return 'ㅀ'
    elif a=='ㅂ' and b=='ㅅ':
        return 'ㅄ'
    else:
        return False
def makingggmo(a,b):
    if a=='ㅗ' and b=='ㅏ':
        return 'ㅘ'
    elif a=='ㅗ' and b=='ㅐ':
        return 'ㅙ'
    elif a=='ㅗ' and b=='ㅣ':
        return 'ㅚ'
    elif a=='ㅜ' and b=='ㅓ':
        return 'ㅝ'
    elif a=='ㅜ' and b=='ㅔ':
        return 'ㅞ'
    elif a=='ㅜ' and b=='ㅣ':
        return 'ㅟ'
    elif a=='ㅡ' and b=='ㅣ':
        return 'ㅢ'
    else:
        return False
        

_JAMO2ENGKEY_ = {
 'ㄱ': 'r',
 'ㄲ': 'R',
 'ㄴ': 's',
 'ㄷ': 'e',
 'ㄸ': 'E',
 'ㄹ': 'f',
 'ㅁ': 'a',
 'ㅂ': 'q',
 'ㅃ': 'Q',
 'ㅅ': 't',
 'ㅆ': 'T',
 'ㅇ': 'd',
 'ㅈ': 'w',
 'ㅉ': 'W',
 'ㅊ': 'c',
 'ㅋ': 'z',
 'ㅌ': 'x',
 'ㅍ': 'v',
 'ㅎ': 'g',
 'ㅏ': 'k',
 'ㅐ': 'o',
 'ㅑ': 'i',
 'ㅒ': 'O',
 'ㅓ': 'j',
 'ㅔ': 'p',
 'ㅕ': 'u',
 'ㅖ': 'P',
 'ㅗ': 'h',
 'ㅘ': 'hk',
 'ㅙ': 'ho',
 'ㅚ': 'hl',
 'ㅛ': 'y',
 'ㅜ': 'n',
 'ㅝ': 'nj',
 'ㅞ': 'np',
 'ㅟ': 'nl',
 'ㅠ': 'b',
 'ㅡ': 'm',
 'ㅢ': 'ml',
 'ㅣ': 'l',
 'ㄳ': 'rt',
 'ㄵ': 'sw',
 'ㄶ': 'sg',
 'ㄺ': 'fr',
 'ㄻ': 'fa',
 'ㄼ': 'fq',
 'ㄽ': 'ft',
 'ㄾ': 'fx',
 'ㄿ': 'fv',
 'ㅀ': 'fg',
 'ㅄ': 'qt'
}


###############################################################################
def is_hangeul_syllable(ch):
    '''한글 음절인지 검사
    '''
    if not isinstance(ch, str):
        return False
    elif len(ch) > 1:
        ch = ch[0]
    
    return 0xAC00 <= ord(ch) <= 0xD7A3

###############################################################################
def compose(cho, jung, jong):
    '''초성, 중성, 종성을 한글 음절로 조합
    cho : 초성
    jung : 중성
    jong : 종성
    return value: 음절
    '''
    if not (0 <= cho <= 18 and 0 <= jung <= 20 and 0 <= jong <= 27):
        return None
    code = (((cho * 21) + jung) * 28) + jong + 0xAC00

    return chr(code)

###############################################################################
# input: 음절
# return: 초, 중, 종성
def decompose(syll):
    '''한글 음절을 초성, 중성, 종성으로 분해
    syll : 한글 음절
    return value : tuple of integers (초성, 중성, 종성)
    '''
    if not is_hangeul_syllable(syll):
        return (None, None, None)
    
    uindex = ord(syll) - 0xAC00
    
    jong = uindex % 28
    jung = ((uindex - jong) // 28) % 21
    cho = ((uindex - jong) // 28) // 21

    return (cho, jung, jong)

###############################################################################
def str2jamo(str):
    '''문자열을 자모 문자열로 변환
    '''
    jamo = []
    for ch in str:
        if is_hangeul_syllable(ch):
            cho, jung, jong = decompose(ch)
            jamo.append( _CHO_[cho])
            jamo.append( _JUNG_[jung])
            if jong != 0:
                jamo.append( _JONG_[jong-1])
        else:
            jamo.append(ch)
    return ''.join(jamo)

###############################################################################
def jamo2engkey(a):
    b=''
    k=_CHO_+_JUNG_+_JONG_
    for i in range(len(a)):
        if a[i] in k:
            b+=_JAMO2ENGKEY_[a[i]]
        else:
            b+=a[i]
    return b

###############################################################################
def engkey2jamo(a):
    b=''
    k=dict(map(reversed,_JAMO2ENGKEY_.items()))
    for i in range(len(a)):
        if a[i] in _JAMO2ENGKEY_.values():
            b+=k[a[i]]
        else:
            b+=a[i]
    return b
###############################################################################
def jamo2syllable(s):
     # 자모 문자열을 음절열로 변환 ('ㄷㅏㄹㄱㄱㅗㄱㅣ' -> '닭고기')
     # 겹자음 : 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'
     # 겹모음 : 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'
    result=[]
    tmp=[]
    k=list(s)
    cjj=_CHO_+_JUNG_+_JONG_
    for i in range(len(k)):
        if not k[i] in cjj:
            return jamo2syllable(s[0:i])+s[i]+jamo2syllable(s[i+1:len(k)])
        else:
            if k[i] in _JUNG_ and len(tmp)==1 and tmp[0] in ggja:
                result.append(decomposggja(tmp[0])[0])
                tmp[0]=decomposggja(tmp[0])[1]
                tmp.append(k[i])
                continue

            if k[i] in _CHO_ and len(tmp)==0:
                tmp.append(k[i])
                continue
            elif k[i] in _JUNG_ and len(tmp)==0:
                tmp.append(k[i])
                continue
            elif tmp[0] in _JUNG_ and k[i] in _JUNG_ and len(tmp)==1:
                if makingggmo(tmp[0],k[i]):
                    result.append(makingggmo(tmp[0],k[i]))
                    tmp=[]
                else:
                    result.append(tmp[0])
                    tmp[0]=k[i]

            elif k[i] in _JUNG_ and len(tmp)==2:
                if makingggmo(tmp[1],k[i]):
                    tmp[1]=makingggmo(tmp[1],k[i])
                    continue
                else:
                    result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),0))
                    tmp=[]
                    tmp.append(k[i])
                    continue
            elif k[i] in _CHO_ and len(tmp)==1:
                if makingggja(tmp[0],k[i]):
                    q=makingggja(tmp[0],k[i])
                    tmp=[]
                    tmp.append(q)
                    continue
                result.append(tmp[0])
                tmp[0]=k[i]
                continue
            elif k[i] in _JUNG_ and len(tmp)==1:
                if tmp[0] in _JUNG_:
                    if makingggmo(tmp[0],k[i]):
                        tmp=[]
                        tmp.append(makingggmo(tmp[0],k[i]))
                        continue
                    else:
                        result.append(tmp[0])
                        tmp=[]
                        tmp.append(k[i])
                        continue
                else:
                    tmp.append(k[i])
                    continue
            elif k[i] in _JONG_ and len(tmp)==2:
                tmp.append(k[i])
                continue
            elif k[i] in _CHO_ and not k[i] in _JONG_ and len(tmp)==2:
                ########################################
                result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),0))
                tmp=[]
                tmp.append(k[i])
                continue
                

            elif k[i] in  _JONG_ and len(tmp)==3:
                if makingggja(tmp[2],k[i]):######
                    tmp.append(k[i])
                    continue
                else:######
                    result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),_jong.index(tmp[2])))
                    tmp=[]
                    tmp.append(k[i])
                    continue
            elif k[i] in  _CHO_ and len(tmp)==3:
                if makingggja(tmp[2],k[i]):######
                    tmp.append(k[i])
                    continue
                else:######
                    result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),_jong.index(tmp[2])))
                    tmp=[]
                    tmp.append(k[i])
                    continue
            
            elif k[i] in _JUNG_ and len(tmp)==4:
                result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),_jong.index(tmp[2])))
                q=tmp[3]
                tmp=[]
                tmp.append(q)
                tmp.append(k[i])
                continue
            elif k[i] in _CHO_ and len(tmp)==4:
                 result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),_jong.index(makingggja(tmp[2],tmp[3]))))
                 tmp=[]
                 tmp.append(k[i])
                 continue

            elif k[i] in  _JUNG_ and len(tmp)==3:
                result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),0))
                q=tmp[2]
                tmp=[]
                tmp.append(q)
                tmp.append(k[i])    
                continue

    if len(tmp)==2 and tmp[0] in _CHO_ and tmp[1] in _JUNG_: #끝처리
        result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),0))
    if len(tmp)==1:
        result.append(tmp[0])
    if len(tmp)==3 and tmp[0] in _CHO_ and tmp[1] in _JUNG_ and tmp[2] in _JONG_:
        result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),_jong.index(tmp[2])))
    if len(tmp)==4 and tmp[0] in _CHO_ and tmp[1] in _JUNG_ and tmp[2] in _JONG_ and tmp[3] in _JONG_:
        if makingggja(tmp[2],tmp[3]):
            result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),_jong.index(makingggja(tmp[2],tmp[3]))))
        else:
            result.append(compose(_cho.index(tmp[0]),_jung.index(tmp[1]),_jong.index(tmp[2])))
            result.append(tmp[3])
    

            


    return ''.join(result)
    

###############################################################################
if __name__ == "__main__":
    
    i = 0
    line = sys.stdin.readline()

    while line:
        line = line.rstrip()
        i += 1
        print('[%06d:0]\t%s' %(i, line)) # 원문
    
        # 문자열을 자모 문자열로 변환 ('닭고기' -> 'ㄷㅏㄺㄱㅗㄱㅣ')
        jamo_str = str2jamo(line)
        print('[%06d:1]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 키입력 문자열로 변환 ('ㄷㅏㄺㄱㅗㄱㅣ' -> 'ekfrrhrl')
        key_str = jamo2engkey(jamo_str)
        print('[%06d:2]\t%s' %(i, key_str)) # 키입력 문자열
        
        # 키입력 문자열을 자모 문자열로 변환 ('ekfrrhrl' -> 'ㄷㅏㄹㄱㄱㅗㄱㅣ')
        jamo_str = engkey2jamo(key_str)
        print('[%06d:3]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 음절열로 변환 ('ㄷㅏㄹㄱㄱㅗㄱㅣ' -> '닭고기')
        syllables = jamo2syllable(jamo_str)
        print('[%06d:4]\t%s' %(i, syllables)) # 음절열

        line = sys.stdin.readline()

