W=input()
n=0
while True:
  T=input().split()
  if T[0]=='END_OF_TEXT':
    break
  for i in T:
    if i.lower()==W.lower():
      n+=1
print(n)
