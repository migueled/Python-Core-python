a = 200
print(id(a))
b = 300
print(id(b))
b = a
print(id(a) == id(b))
print(a is b)

c = 1
print(id(c))
c +=1
print(id(c))

d = [1, 2, 3, 4]
print(d)
e = d
e[0] = 2
print(d)
print(d is e)

#Value vs indentity equality
f = [0, 1, 2, 3, 4]
g = [0, 1, 2, 3, 4]
print(f == g)
print(f is g)