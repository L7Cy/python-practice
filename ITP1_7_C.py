r,c=map(int,input().split())
a=[input().split() for i in range(r)]
r_sum=0
c_sum=0
sum=0
for i in range(r):
  for j in range(c):
    r_sum+=int(a[i][j])
    print(a[i][j],end="")
    print(" ",end="")
  print(r_sum)
  r_sum=0
for i in range(c):
  for j in range(r):
    c_sum+=int(a[j][i])
    sum+=int(a[j][i])
  print(c_sum,end="")
  print(" ",end="")
  c_sum=0
print(sum)
