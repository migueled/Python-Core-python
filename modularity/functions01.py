def square(x):
    return x * x

def launchMissiles():
    print('Missiles launch!')

print(square(5))
launchMissiles()

def evenOrOdd(n):
    if n % 2 == 0:
        print('even')
        return
    print ('odd')

w = evenOrOdd(31)
print(w is None)

def nthRoot( radicand, n):
    return radicand ** (1/n)

print(nthRoot(16,2))
print(nthRoot(27,3))