def inputconvert():
    f = []
    while True:
        t = input()
        if t:
            f.append(t)
        else:
            break
    return f

s = 0
k = 0
b = []
c = []
a = inputconvert()
for i in a:
    if i.isdigit():
        s = s + int(i)
        b.append(int(i))
    if i.isalpha():
        k = k + 1
        c.append(i)

print(s)
print(k)
print(b)
print(c)