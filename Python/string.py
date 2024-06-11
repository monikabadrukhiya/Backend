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
schar="!@#$%^&*()_+{}[]:;<>,.?\\/-"
cnt=0
n=input("Enter string=")
for i in range(0,len(n)):
    # if(n[i]>=31 and n[i]<=47 or n[i]>=58 and n[i]<=64 or n[i]>=91 and n[i]<=96 
    #    or n[i]>=122 and n[i]<=126):
    if n[i]==schar:
        print("-----")
        cnt=cnt+1
print("special char=",cnt)

# ===========upper to lower char convert=============
# n=input("Enter string=")
# new=n.lower()
# print(new)

