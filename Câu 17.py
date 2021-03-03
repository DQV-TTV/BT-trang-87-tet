def inputconvert():
    f = []
    while True:
        t = input()
        if t:
            f.append(t)
        else:
            break
    return f

a = []
b = []
f = []
c = []
d = []
#################################
c = inputconvert()
d = inputconvert()
#################################
for i in c:
    if i.isdigit():
        a.append(int(i))
for i in d:
    if i.isdigit():
        b.append(int(i))
#################################
if len(a) < len(b):
    v = b.copy()
    for i in range(len(a)):
        f.append(a[i] + b[i])
        del v[0]

    for i in v:
        f.append(i)
#################################
if len(a) > len(b):
    v = a.copy()
    for i in range(len(b)):
        f.append(a[i] + b[i])
        del v[0]

    for i in v:
        f.append(i)
#################################
print(f)