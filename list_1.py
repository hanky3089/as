a = [3, "1", 4, 2]
print(a[2])
print(a[-1])
a.append(5)
print(a)
a[1]=1
print(a)

b=a[1:3]
print(b)

c = a[2:]
print(c)

d = a[1:-1]
print(d)

e = a[2:-1]
print(e)
f = []
for el in a:
    f.append(el)
f[0]=99
print(a,f,sep="\n")

g = a+[10,20]
print(g)

a[2:4]=[7,8,9]
print(a)