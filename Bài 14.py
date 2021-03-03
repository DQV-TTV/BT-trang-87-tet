def inputconvert():
    f = []
    while True:
        t = input()
        if t:
            f.append(t)
        else:
            break
    return f

a = inputconvert()
b = []
for i in a:
    if i.isdigit():
        b.append(int(i))
    if i.isalpha() == False and i.isdigit() == False:
        b.append(float(i))
print(b)