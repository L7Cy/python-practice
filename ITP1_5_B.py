while True:
  h,w=map(int,input().split())
  if (h==0)and(w==0):
    break
  for i in range(h):
    for j in range(w):
      if (j==0)or(j==w-1)or(i==0)or(i==h-1):
        print("#",end="")
      else:
        print(".",end="")
    print()
  print()
