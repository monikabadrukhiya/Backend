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

# ==========ascending  array===============
# n=([43,46,76,78,54,12,0,38,54])
# temp=0
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if(n[i]>n[j]):
#             temp=n[i]
#             n[i]=n[j]
#             n[j]=temp
#     print(n[i])

# ==========deccending  array===============
# n=([43,46,76,78,54,12,0,38,54])
# temp=0
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if(n[i]<n[j]):
#             temp=n[i]
#             n[i]=n[j]
#             n[j]=temp
#     print(n[i])

# =============position add======================
# n=([43,46,76,78,54,12,0,38,54])
# pos=5
# value=100
# for i in range(len(n)-1,-1):
#     n[i]=n[i-1]
# n[pos]=value
# for i in range(0,len(n)):
#     print(n[i])

# ============ position delete =================
# n=([43,46,76,78,54,12,0,38,54])
# pos=2
# for i in range(pos,len(n)-1):
#     n[i]=n[i+1]
# for i in range(0,len(n)-1):
#     print(n[i])

# ============ reverse tuple===============
# n=([43,46,76,78,54,12,0,38,54])
# print(n)
# new=([])
# for i in range(len(n)-1,-1,-1):
#     new=new+[n[i]]
# list=new
# print(list)

# ============multiple value delete=========
# m=int(input("enter n="))
# n=([43,46,76,78,54,12,0,38,54,12])
# new=[]
# for i in range(len(n)):
#     if n[i]!=m:
#         new=new+[n[i]]
# list=new
# print(list)







