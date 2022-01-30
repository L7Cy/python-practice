s=input()

def solve(query):
  while 1:
    print(query)
    for flag in ("erase","eraser","dream","dreamer"):
      if query.endswith(flag):
        query = query[:-len(flag)]
        break
    else:
      print("NO")
      break
    if not query:
      print("YES")
      break
solve(s)
