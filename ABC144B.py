n=int(input())
c=0
for i in range(9):
  if int(n/(i+1))<=9 and n%(i+1)==0:
    print('Yes')
    c+=1
    break
if c==0:
  print('No')
