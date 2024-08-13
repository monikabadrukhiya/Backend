# ========  filter function in list ==============
# list=[45,23,10,5,67,98,18]
# def Value(n):
#     if n>=18:
#         return n
# get=filter(Value,list)
# a=[]
# for i in get:
#     a.append(i)
# print(a)

# ================= filter function in pelidrome ========================
i=[121,234,2,34,56,5776,756,1]
def Value(i):
        n=i
        sum=0
        rem=0
        while(n!=0):
            rem=n%10
            sum=sum*10+rem
            n=n//10
            if sum==i:
              return sum  
get=filter(Value,i)
ans=[]
for i in get:
    ans.append(i)
print(ans)

