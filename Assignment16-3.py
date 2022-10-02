print("Enter the elements sepreted by comman:")
x=tuple([eval(i) for i in input().split(',')])
print(x)
print(x[::-1])
