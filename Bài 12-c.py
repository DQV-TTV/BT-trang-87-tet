n = int(input())
d = []
s = 0

for i in range(2,((n-1)*n)+1):
    d.append(i)

print("\n")
for i in range(n+1):
    for j in d:
        if j == (i-1)*i:
            print("{ " + str(j) + " }")
            s = s +1/j

print("\n")
print("Hello  " + str(s))
print("\n")
print(d)
