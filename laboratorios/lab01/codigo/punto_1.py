import sys
from time import time
sys.setrecursionlimit(1000000000)
def maxsec(str1,str2):
    if len(str1)==0 or len(str2)==0:
        return 0
    if str1[len(str1)-1]==str2[len(str2)-1]:
        return 1+maxsec(str1[:len(str1)-1],str2[:len(str2)-1])
    return max(maxsec(str1[:len(str1)-1],str2),maxsec(str1,str2[:len(str2)-1]))

def area(n):
    if (n<=2):
        return n
    return area(n-1)+area(n-2)



for i in range(20,40):
    start =time()
    area(i)
    tiempo= time()-start
    print(tiempo)




