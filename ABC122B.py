s=input()
counta=0
max=0
for i in range(len(s)):
  if s[i]=='A' or s[i]=='C' or s[i]=='G' or s[i]=='T':
    counta+=1
  else:
    if max<counta:
      max=counta
    counta=0
  if max<counta:
    max=counta
print(max)
