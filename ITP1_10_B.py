import math
a,b,c=map(float,input().split())
c=math.radians(c)
s=a*b*math.sin(c)/2
l=a+b+math.sqrt(a**2+b**2-2*a*b*math.cos(c))
h=2*s/a
print(s)
print(l)
print(h)
