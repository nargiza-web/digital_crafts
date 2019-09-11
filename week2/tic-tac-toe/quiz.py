
'''x = 1
def test():
    x = 2
test() 
print(x) # 1 correct!!!!


x = 1
def test():
    global x
    x = 2
test()
print(x) # 2 correct!!!


x = [1]
def test():
    x = [2]
test()
print(x) #2 wrong


x = [1]
def test():
    global x
    x = [2]
test()
print(x) #2 correct!!!


x = [1]
def test():
    x[0] = 2
test()
print(x)#2 correct!!!'''
