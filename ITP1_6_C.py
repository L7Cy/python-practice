n=int(input())
buildings=[[[0 for b in range(10)] for f in range(3)] for r in range(4)]
x=0
for i in range(n):
  b,f,r,v=map(int,input().split())
  buildings[b-1][f-1][r-1]+=v
for floors in buildings:
  for rooms in floors:
    for persons in rooms:
      print(" ", end="")
      print(persons, end="")
    print()
  x=x+1
  if x!=4:
    print("####################")
