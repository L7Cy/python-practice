n=int(input())
counta=0
while(n>0):
  if len(str(n))%2==1:
    counta+=1
  n-=1
print(counta)
