# 1.no argument ,no return==============
def sum():
    print("hello")
sum()

# 2.with argument,no return=============
def sum(a):
    print(a)
sum(10)

def sum1(a,b):
    print("a=",a,"b=",b)
sum1(10,"hii")

# 3.with argument ,with return============
def sum(a,b):
    return a+b
sum(10,20)
c=sum(10,20)
print(c)

# 4. no argument,with return==============
def sum():
    a=1
    b=2
    return a+b
print(sum())
