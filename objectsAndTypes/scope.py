#Rebinding global names
count = 0
def showCount():
    print(count)

def setCount(c):
    count = c
 
showCount()
setCount(5)
showCount()

def setcount(c):
    global count
    count = c

showCount()
setcount(5)
showCount()
