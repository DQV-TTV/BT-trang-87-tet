n = int(input())
a = []
b = []
for i in range(0,n+1,2):
    if i<n:
        a.append(i)
for i in range(1,n+1,2):
    if i<n:
        b.append(i)

print(a)
print(b)