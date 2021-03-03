def inputconvert():
    f = []
    d = []
    while True:
        t = input()
        if t:
            f.append(t)
        else:
            break
    for i in f:
        d.append(int(i))
    return d

c = []
a = inputconvert()
b = inputconvert()
for i in a:
    c.append(i)
for i in b:
    c.append(i)
c.sort()
print(c)