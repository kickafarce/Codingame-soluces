s=lambda:input().split()
a=s()
t={a[3]:a[4]}
for i in range(int(a[7])):
 u,v=s()
 t[u]=v
while t:
 d,c,h=s()
 try:k=int(c)-int(t[d])
 except:k=0
 print(['WAIT','BLOCK'][('R'in h)&(k>0)|('L'in h)&(k<0)])