n,m,l=map(int,input().split())
a=[input().split() for i in range(n)]
b=[input().split() for i in range(m)]
c=[[0 for j in range(l)] for i in range(n)]
for i in range(n):
  for j in range(l):
    for k in range(m):
      c[i][j]+=int(a[i][k])*int(b[k][j])
for i in range(n):
  for j in range(l):
    print(c[i][j],end="")
    if j<l-1:
      print(" ",end="")
  print()
