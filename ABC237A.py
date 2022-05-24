n=int(input())
if n>=-2**31:
  if n<2**31:
    print("Yes")
  else:
    print("No")
else:
  print("No")
