import random

n,t=map(int,input().split())
if n==6:
  threshold=18
elif n==7:
  threshold=25
elif n==8:
  threshold=33
elif n==9:
  threshold=45
elif n==10:
  threshold=51
tile=list(list(input()) for i in range(n))
for y in range(n):
  for x in range(n):
    tile[y][x]=format(int(tile[y][x],16),'04b')
counta=10
pre_s=''
while(counta<t):
  horizon=0
  for y in range(n):
    for x in range(n):
      if tile[y][x]=='0000':
        strs='DRUL'
        if x!=n-1 and y!=n-1 and x!=0 and y!=0:
          down=tile[y+1][x]
          right=tile[y][x+1]
          up=tile[y-1][x]
          left=tile[y][x-1]
          if down[2]==0:
            strs+='DDDD'
          if right[3]==0:
            strs+='RRRR'
          if up[0]==0:
            strs+='UUUU'
          if left[1]==0:
            strs+='LLLL'
        s=''.join(random.sample(strs,1))
        if s=='D' and y!=n-1 and pre_s!='U':
          print(s,end='')
          counta+=1
          tile[y][x],tile[y+1][x]=tile[y+1][x],tile[y][x]
        elif s=='R' and x!=n-1 and pre_s!='L':
          print(s,end='')
          counta+=1
          tile[y][x],tile[y][x+1]=tile[y][x+1],tile[y][x]
        elif s=='U' and y!=0 and pre_s!='D':
          print(s,end='')
          counta+=1
          tile[y][x],tile[y-1][x]=tile[y-1][x],tile[y][x]
        elif s=='L' and x!=0 and pre_s!='R':
          print(s,end='')
          counta+=1
          tile[y][x],tile[y][x-1]=tile[y][x-1],tile[y][x]
        pre_s=s
      if x!=n-1:
        right=tile[y][x+1]
        left=tile[y][x]
        if left[1]==right[3]=='1':
          horizon+=1
      if y!=n-1:
        up=tile[y][x]
        down=tile[y+1][x]
        if up[0]==down[2]=='1':
          horizon+=1
      if horizon>=threshold:
        counta+=t
