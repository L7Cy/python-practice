while(True):
  n=int(input())
  if n==0:
    break
  s=list(map(int,input().split()))
  m=sum(s)/n
  a_2_n=0
  for i in range(n):
    a_2_n=a_2_n+(s[i]-m)**2
  print((a_2_n/n)**0.5)
