# 1st way

func1 = lambda x : x +25
print(func1(10))

# 2st way

def func2(y= 25):
    return lambda z : y + z

result = func2()
print(result(10))