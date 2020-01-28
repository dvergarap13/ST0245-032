def gcd_euclid(p, q):
    if (q==0):
        return p
    return gcd_euclid(q,p%q)


print(gcd_euclid(60, 48))

  
def Suma_grupo(start, nums, target):
    if (start>=len(nums)):
        return target==0;
    return Suma_grupo(start+1,nums, target-nums[start]) or Suma_grupo(start+1,nums,target)


print(Suma_grupo(0,[2, 4, 8],10))


  
def subconjuntos(s):
    subconjuntosBase("", s)

def subconjuntosBase(base, t):
    if (t==""):
        print (base)
    else:
        subconjuntosBase(base+t[0], t[1:]) 
        subconjuntosBase(base,t[1:])
        

print(subconjuntos("abc"))