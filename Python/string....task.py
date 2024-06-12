# ===========split string and count char==================
# a="creative"
# count=0
# for i in range(0,len(a)):
#     print(a[i])
#     count=count+1
# print("count== ",count)

# ==============find upper character==================
# count1=0
# n=input("Enter string = ")
# for i in range(0,len(n)):
#     if(n[i]>='A' and n[i]<='Z'):
#         count1=count1+1
# print("upper char=",count1)

# =========== find lower character ================
# count2=0
# n=input("Enter string = ")
# for i in range(0,len(n)):
#     if(n[i]>='a' and a[i]<='z'):
#         count2=count2+1
# print("lower char =",count2)

# ============ special char count ==================
n=input("Enter string=")
count=0
for i in range(len(n)):
    if(n[i]=='!' or n[i]=='@' or n[i]=='#'or n[i]=='$'or n[i]=='%' or n[i]=='^'or 
       n[i]=='&' or n[i]=='*'):
        count=count+1
print("special char=",count)

# ===========upper to lower char convert=============
# n=input("Enter string=")
# new=n.lower()
# print("up to lower char="new)

# =========lower to upper char convert=============
# n=input("Enter string=")
# new=n.upper()
# print("lower to upper char ="new)

