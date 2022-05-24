n,m=map(int,input().split())
A=[list(map(int,input().split())) for i in range(n)]
b=[]
c=[0 for i in range(n)]
for _ in range(m):
  b.append(int(input()))
for i in range(n):
  for j in range(m):
    c[i-1]+=A[i-1][j-1]*b[j-1]
for i in range(n):
  print(c[i])
