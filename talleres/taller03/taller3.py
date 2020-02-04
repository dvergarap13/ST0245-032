#!/usr/bin/python

def hanoi(topN, a, b, c):
    if topN>=1:
        hanoi(topN-1,a,c,b)
        mover(a,c)
        hanoi(topN-1,b,a,c)

def mover(inicio, fin):
    print("mover un disco de la "+inicio + " a "+fin)
    
hanoi(5,"torre 1","torre 2","torre 3")    

def permutations(base, stri):
    if (stri==""):
        print (base)
    else:
        for i in range(len(stri)):
            permutations(base+stri[i], stri[:i]+stri[i+1:])

permutations("","abcd")
    
