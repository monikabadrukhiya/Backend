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
list=["moni","mansi","khushal","kinjal","keyuri","panvi","kajal","panthi","prutha"]
for i in range(0,len(list)):
    if(list[i][0]=='p'):
        print(list[i])
    
