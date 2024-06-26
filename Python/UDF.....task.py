# =====================reverse value and check same or not==================
# method:1
# def rev(n):
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
#     return(sum)
# n=int(input("Enter value="))
# c=rev(n)
# print(c)
# def check(c,n):
#     if(c==n):
#         print("yes")
#     else:
#         print("no")
# print=check(c,n)

# =====================method:2==================
# def rev(n):
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
#     return(sum)
# n=int(input("Enter no="))
# c=rev(n)
# print("reverse value=",c)

# def check(n,c):
#     return n==c
# k=check(n,c)
# if(k==1):
#     print("both are same")
# else:
#     print("different")

# ===================spy number====================
# def spy(n):
#     sum=0
#     multi=1
#     while(n!=0):
#         rem=n%10
#         sum=sum+rem
#         multi=multi*rem
#         n=n//10
#     return(sum==multi)    
# n=int(input("Enter no="))
# s=spy(n)
# # print("spy",s)
# def check(s,n):   
#     if(s==1):
#         print("spy no")
#     else:
#         print("not spy num")
# check(s,n)

        # ==========  method : 2  ========================
def sum(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+rem
        n=n//10
    return(sum)
def multi(n):
    multi=1
    while(n!=0):
        rem=n%10
        multi=multi*rem
        n=n//10
    return(multi)
n=int(input("Enter no="))
a=sum(n)
b=multi(n)
print("sum=",a)
print("multi=",b)

def check(a,b):
    if(a==b):
        print("its spy num")
    else:
        print("its not spy num")
check(a,b)
