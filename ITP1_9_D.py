str=input()
q=int(input())
for i in range(q):
  command=input().split()
  if command[0]=='replace':
    str=str[:int(command[1])]+command[3]+str[int(command[2])+1:]
  elif command[0]=='reverse':
    tmp=str[int(command[1]):int(command[2])+1]
    str=str[:int(command[1])]+tmp[::-1]+str[int(command[2])+1:]
  elif command[0]=='print':
    print(str[int(command[1]):int(command[2])+1])
