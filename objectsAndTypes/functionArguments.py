# Default arguments values
def banner(message, border = '-'):
    line = border * len(message)
    print(f'{line}\n{message}\n{line}')

banner('Norwegian blue')
banner('Norwegian blue', '*')

banner('Sun, moon and stars', border = '*')
banner(border = '.', message = 'Hello from earth')

#Default value evaluation
import time
time.ctime()

def showDefault(arg = time.ctime()):
    print(arg)

showDefault()
showDefault()
showDefault()

#Mutable default values
def addSpam(menu = []):
    menu.append('spam')
    return menu

breakfast = ['bacon', 'eggs']
print(addSpam(breakfast))
launch = ['baked beans']
print(addSpam(launch))
print(addSpam())
print(addSpam())
print(addSpam())

#Inmutanle default value
def addSpamTwo( menuTwo = None):
    if menuTwo is None:
        menu = []
    menu.append('spam')
    return menu

print(addSpamTwo())
print(addSpamTwo())
print(addSpamTwo())