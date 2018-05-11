x=[2,3,4]
for i in x:
    print(i, end=" ")
print()

for i in range(len(x)):
    print(x[i], end=" ")
print()

for idx, i in enumerate(x) :
    print(idx+1,i,sep=":") 
print()

x.append(5)
print(x)

y=[1,2]
z=x+y
print(x,y,z,sep="\n")

z=x
z[0]=99
print(x,z,sep="\n")

x.append(y)
print(x)


print(x)
x[1:3]=[90,91,92]
print(x)