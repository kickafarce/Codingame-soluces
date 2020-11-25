s=lambda:input().split()
a=s()
t={a[3]:a[4]}
n=int(a[7])
while n:
 u,v=s()
 t[u]=v
 n-=1
while t:
 d,c,h=s()
 k=int(c)-int(t[d])if d in t else 0
 print(['WAIT','BLOCK'][('R'in h)&(k>0)|('L'in h)&(k<0)])
