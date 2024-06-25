# ============string print in tuple array=========
# name=('moni','kinjal','panvi')
# print(name)

# ========find sum===================
# sum=0
# list=(29,49,59,69,10,20)
# for i in range(0,len(list)):
#     sum=sum+list[i]
# print("sum=",sum)

# =============find minimun===========
# n=(29,49,59,69,10,20)
# min=n[0]
# for i in range(0,len(n)):
#     if(min>n[i]):
#         min=n[i]
# print("min=",min)

# =============find maximun===========
# n=(29,49,59,69,10,20)
# min=n[0]
# for i in range(0,len(n)):
#     if(min<n[i]):
#         min=n[i]
# print("min=",min)

# ============== pass char string return=====================
# n=("moni","mansi","khushal","kinjal","keyuri","panvi","kajal","panthi","prutha")
# for i in range(0,len(n)):
#     if(n[i][0]=='p'):
#         print(n[i])

# ==========ascending  array===============
# n=([43,46,76,78,54,12,0,38,54])
# temp=0
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if(n[i]>n[j]):
#             temp=n[i]
#             n[i]=n[j]
#             n[j]=temp
# new=tuple(n)
# print(new)

# ==========deccending  array===============
# n=([43,46,76,78,54,12,0,38,54])
# temp=0
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if(n[i]<n[j]):
#             temp=n[i]
#             n[i]=n[j]
#             n[j]=temp
# new=tuple(n)
# print(new)

# =============position add======================
# n=([43,46,76,78,54,12,0,38,54])
# pos=5
# value=100
# for i in range(len(n)-1,-1):
#     n[i]=n[i-1]
# n[pos]=value
# for i in range(0,len(n)):
#   new=tuple(n)
# print(new)

# ============ position delete =================
# n=([43,46,76,78,54,12,0,38,54])
# pos=2
# new=[]
# for i in range(len(n)):
#     if i!=pos:
#         new=new+[n[i]]
# arr=tuple(new)
# print(arr)

# ============ reverse tuple===============
# n=([43,46,76,78,54,12,0,38,54])
# print(n)
# new=([])
# for i in range(len(n)-1,-1,-1):
#     new=new+[n[i]]
# new1=tuple(new)
# print(new1)

# ============multiple value delete=========
# m=int(input("enter n="))
# n=([43,46,76,78,54,12,0,38,54,12])
# new=[]
# for i in range(len(n)):
#     if n[i]!=m:
#         new=new+[n[i]]
# new1=tuple(new)
# print(new1)

# =========count how time value repeat in tuple ===============
# n=(13,45,65,67,45,87,89,20)
# value=45
# count=0
# for i in range(0,len(n)):
#     if (n[i]==value):
#         count=count+1
# print(count,"time repeat",value)

# ===========user input value and print that value===============
# n=int(input("Enter n="))
# newarr=[]
# for i in range(n+1):
#     name=input("Enter name=")
#     newarr.append(name)
# new=tuple(newarr)
# print(new)

# ============find value divide by 5 & 7 and convert into list================
n=(20,47,40,45,50,65,2,30,22,42,14)
print(n)
new=[]
for i in n:
    if(i%5 or i%7==0):
        new.append(i)
arr=(new)
print(arr)





