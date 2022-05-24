s=input()

def solve(query):
  while 1:
    if str(query)==str(query)[len(query)::-1]:
      print("Yes")
      break
    for i in range(10**6):
      if query.endswith("a"):
        query = query[:-1]
        break
    else:
      print("No")
      break
solve(s)
