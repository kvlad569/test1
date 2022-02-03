l = [10, 30, 28, 4, 11, 39]

r = []
n = len(l)
for i in range(0, n):
    r.append(min(l))
    l.remove(min(l))

print(r)















