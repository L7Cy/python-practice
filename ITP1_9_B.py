while True:
  str = input()
  if str == '-':
    break
  m = int(input())
  for i in range(m):
    h = int(input())
    str = str[h:] + str[:h]
  print(str)
