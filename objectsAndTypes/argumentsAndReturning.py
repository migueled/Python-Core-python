# Argument passing
m = [9, 15, 24]
def modify(k):
    k.append(39)
    print(f'k = {k}')

modify(m)
print(m)

print('---------------------')
# Replacing argument value
f = [14, 23, 37]
def replace(g):
    g = [17, 28, 45]
    print(f'g = {g}')

replace(f)
print(f)

print('---------------------')
# Mutable arguments
def replaceContents(l):
    l[0] = 17
    l[1] = 28
    l[2] = 45
    print(f'l = {l}')

x = [14, 23, 37]
replaceContents(x)
print(x)

print('---------------------')
# Return semantics
def y(z):
    return z

m = [6, 10, 16]
n = y(m)
print(m is n)