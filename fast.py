l = [[0,1,1],
     [1,0,1],
     [0,0,1]]
lx = []
ly = []
output = []
out = []

#ly zeile zusammenschieben
for r in range(len(l)):
    n = 0
    for r2 in range(len(l[r])):
        if l[r][r2]==0:
            n -= 1
        else: n += 1
    ly.append(n)

#lx
for r in range(len(l[0])):
    n = 0
    for r2 in range(len(l)):
        if l[r2][r]==0:
            n -= 1
        else: n += 1
    lx.append(n)

for r in range(len(l)):
    if r != 0:
        output.append(out)
    out = []
    for r2 in range(len(l[0])):
        out.append(lx[r2]+ly[r])
output.append(out)
print(output)
