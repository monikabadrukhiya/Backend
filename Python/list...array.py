# =========== find static char================
# list=["creative","monika","panvi","khushal"]
# print(list[2][4])


# ============ array sum==================
# sum=0
# list=[12,34,56,78,98]
# for i in range(0,len(list)):
#     sum=sum+list[i]
# print("sum= ",sum)

# ================ array min=================

# n=[24,65.12,43,4,76,58,1]
# min=n[0]
# for i in range(0,len(n)):
#     if min>n[i]:
#         min=n[i]
# print("min=",min)

# ============ array max ==================
# n=[34,54,56,87,98,12,48]
# max=n[0]
# for i in range(0,len(n)):
#     if(max<n[i]):
#         max=n[i]
# print("max= ",max)


# =============== accending array value ==============
# n=[43,46,76,78,54,12,0,38,54]
# temp=0
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if(n[i]>n[j]):
#             temp=n[i]
#             n[i]=n[j]
#             n[j]=temp
#     print(n[i])

# =============== deccending array value==================
# n=[43,46,76,78,54,12,0,38,54]
# temp=0
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if(n[i]<n[j]):
#             temp=n[i]
#             n[i]=n[j]
#             n[j]=temp
#     print(n[i])

# ============== pass char string return=====================
# list=["moni","mansi","khushal","kinjal","keyuri","panvi","kajal","panthi","prutha"]
# for i in range(0,len(list)):
#     if(list[i][0]=='p'):
#         print(list[i])


# ====================== insert valuse spesific position ===============

# n=[10,30,45,67,87,37,98,49,100,15]
# pos=4
# value=200
# n=n+[0]
# for i in range(len(n)-1,pos,-1):
#     print("==========")
#     n[i]=n[i-1]
# n[pos]=value

# for i in range(0,len(n)):
#    print(n[i])
    
# ================= delete value specific position ===================
pos=5
n=[10,30,45,67,87,37,98,49,100,15]
for i in range(pos,len(n)-1):
    n[i]=n[i+1]

for i in range(0,len(n)-1):
    print(n[i])
