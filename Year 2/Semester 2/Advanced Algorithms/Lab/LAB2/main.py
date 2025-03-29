import math 

aux = input().split()
a, b = int(aux[0]), int(aux[1])
p = int(input())
m = int(input())
l = math.ceil(math.log((b - a) * 10 ** p, 2))
d = (b - a) / 2 ** l
sol = []

for _ in range(m):
    op = input()
    if op[0] == 'T':
        x = float(input())
        i = 0
        while x >= a:
            x -= d 
            i += 1
        x += d
        i -= 1

        aux = 2 ** (l - 1)
        t = [0] * l
        for x in range(l):
            if i - aux >= 0:
                i -= aux 
                t[x] = 1
            aux >>= 1
        sol.append("".join([str(y) for y in t]))
        
    else:
        x = input().rstrip("\n")
        y = 0
        j = 0
        for i in range(l - 1, -1, -1):
            y += (2 ** j * int(x[i]))
            j += 1
        sol.append(a + y * d)
    
for x in sol:
    print(x)
            