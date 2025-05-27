from multipledispatch import dispatch

#Sum
@dispatch(int,int)
def sum(w,r):
    return w+r

@dispatch(int,int,int)
def sum(w,r,x):
    return w+r+x

print(sum(2,3))
print(sum(4,5,6))

#product
@dispatch(int,int)
def multiply(a,b):
    return a*b

@dispatch(int,int,int)
def multiply(x,y,z):
    return x*y*z

print(multiply(4,5))
print(multiply(2,3,4))


@dispatch(int,int,int)
def sum(x,y,z):
    result = x+y+z
    print(result)

@dispatch(float,float)
def sum(a,b):
    result = a+b
    print(result)

sum(1,2,4)
sum(2.2,5.1)