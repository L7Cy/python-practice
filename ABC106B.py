n=int(input())
counta=0
sum=0
for i in range(n):
  if (i+1)%2==1:
    for j in range(i+1):
      if (i+1)%(j+1)==0:
        counta+=1
    if counta==8:
      sum+=1
  counta=0
print(sum)
