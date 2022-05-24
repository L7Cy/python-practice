while True:
  n,x=map(int,input().split())
  if n==0 & x==0:
    break
  m=0
  for i in range(1,n+1):
    for j in range(1,i):
      k=x-(i+j)
      if k < j and k <= n and k > 0:
        m+=1
  print(int(m))
