# =========== 1 to 10 digit===========
# for i in range(10):
#     print(i)

# for j in range(10,0,-1):
#     print(j)

# for i in range(1,10,3):
#     print(i)


# arr=['moni','panvi','khushal']
# for w in arr:
#     print(w,len(w))

# =========== 1 to n digit sym=============
# n=int(input("Enter n="))
# sum=0
# for i in range(1,n):
#     print(i)
#     sum=sum + i
# print("sum= ",sum)

# ============ digonal sum===========
# n=int(input("Enter n="))
# sum=0
# for i in range(1,n):
#     sum=sum+i
#     print(i,"=",sum)

# ============== table ===============
# n=int(input("Enter n="))
# i=1
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# ============= print even num into 1 to n number and sum that num=========
# n=int(input("Enter n="))
# sum=0
# for i in range(1,n+1):
#     if(i%2==0):
#         print(i)
#         sum=sum+i
# print("sum=",sum)

# ============= print odd num into n to 1 number and sum that num=========
# n=int(input("Enter n="))
# sum=0
# for i in range(n,0,-1):
#     if(i%2==1):
#         print(i)
#         sum=sum+i
# print("sum of odd num =",sum)

# =============== factorial ===============
# n=int(input("Enter n="))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial= ",fact)

# ============ Reverse=============
# n=int(input("Enter n="))
# sum=0
# for i in range(n):
#     if(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
# print("reverse=",sum)

# =================pelidrom num===============
# n=int(input("Enter n="))
# sum=0
# a=n
# for i in range(n):
#     if(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
# if(sum==a):
#     print("its pelidrom num")
# else:
#     print("its not pelidrom")

# =============== Armstrong num ===============
# n=int(input("Enter n="))
# sum=0
# a=n
# for i in range(n):
#     if(n<=1000):
#         rem=n%10
#         sum=sum+(rem*rem*rem)
#         n=n//10
# if(sum==a):
#     print("its armstron num")
# else:
#     print("its not armstrong num")

# =============spy num================
# n=int(input("Enter n="))
# sum=0
# multi=1
# for i in range(n):
#     if (n!=0):
#         rem=n%10
#         sum=sum+rem
#         multi=multi*rem
#         n=n//10
# if(sum==multi):
#     print("its spy num")
# else:
#     print("its not spy num")

# ================ neon num ========================
# n=int(input("Enter n="))
# sum=0
# neon=n*n
# for i in range(neon):
#     if(neon!=0):
#         rem=neon%10
#         sum=sum+rem
#         neon=neon//10
# if(sum==n):
#     print("its neon num")
# else:
#     print("its not neon num")

# =================pelidrom series=========================
# for i in range(10,1000):
#     n=i
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10 
#     if(sum==i):
#         print(sum,end=" ")

# ================ Armstrong series ==============================
# for i in range(1,1000):
#     sum=0
#     n=i
#     while(n!=0):
#         rem=n%10
#         sum=sum+(rem*rem*rem)
#         n=n//10
#     if(sum==i):
#         print(sum,end=" ")

# ============== spy series===========================================
# for i in range(1,1000):
#     sum=0
#     muulti=1
#     n=i
#     while(n!=0):
#         rem=n%10
#         sum=sum+rem
#         muulti=muulti*rem
#         n=n//10
#     if(sum==muulti):
#         print(i,end=" ")

# ===================== Neon Num ==================================
for i in range(1,100):
    sum=0
    neon=i*i
    while(neon!=0):
        rem=neon%10
        sum=sum+rem
        neon=neon//10
    if(sum==i):
        print(sum,end=" ")








