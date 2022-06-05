n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
d_1=0
d_2=0
d_3=0
d_inf=0
for i in range(n):
  d_1+=abs(x[i]-y[i])
  d_2+=abs(x[i]-y[i])**2
  d_3+=abs(x[i]-y[i])**3
  if abs(x[i]-y[i])>d_inf:
    d_inf=abs(x[i]-y[i])
print(d_1)
print(d_2**0.5)
print(d_3**(1/3))
print(d_inf)
