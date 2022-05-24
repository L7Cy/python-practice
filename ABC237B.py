n, m = [int(i) for i in input().split()]
table = [[int(i) for i in input().split()] for n in range(n)]
tr = []
for i in range(m):
    tr_row = []
    for vector in table:
        tr_row.append(vector[i])
    tr.append(tr_row)
for a in tr:
  print(*a)
