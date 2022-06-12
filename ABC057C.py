n=int(input())
min=10000000000
for i in range(int(n**0.5)+1):
  if n%(i+1)==0:
    f1=len(str(i+1))
    f2=len(str(int(n/(i+1))))
    if f1>=f2:
      f=f1
    else:
      f=f2
  if min>f:
    min=f
print(min)
