n=int(input())
s=input()
counta=0
for i in range(n-2):
  if s[i:i+3]=='ABC':
    counta+=1
print(counta)
