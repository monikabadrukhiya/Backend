# ======in loop code multiple time can exicute
# ==== 1 to 10 digit ====
# i=1
# while (i<=10):
#     print(i)
#     i=i+1

# ====n digit sum====
# n=int(input("Enter n="))
# sum=0
# i=1
# while(i<=n):
#     sum=sum+i
#     i=i+1
    
# print("sum=",sum)

# ======table=======
# n=int(input("Enter n="))
# i=1
# while(i<=10):
#     print(n,"*"i,"=" n*i)
#     i=i+1

# =============digonal sum====================
# n=int(input("Enter n="))
# sum=0
# i=1
# while(i<=10):
#     sum=sum+i
#     print(i,"=",sum)
#     i=i+1

# ========find even num and sum that num========

# n=int(input("Enter n="))
# sum=0
# i=1
# while(i<=n):
#     if(i%2==0):
#         print(i)
#     sum=sum+i
#     i=i+1
# print("sum=",sum)

# ===========factorial=========================
# n=int(input("Enter n="))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i=i+1
# print("fact=",fact)


# ==============indivisul digit sum=====================
# n=int(input("Enter n="))
# rem=0
# sum=0
# while(n!=0):
#     rem=n%10
#     sum=sum+rem
#     n=n//10
# print("indivisul digit sum = ",sum)

# =================reverse==============
# n=int(input("Enter n="))
# sum=0
# rem=0
# while(n!=0):
#     rem=n%10
#     sum=sum*10+rem
#     n=n//10
# print("reverse = ",sum)

# ==============pelidrom number===============
# n=int(input("Enter n="))
# sum=0
# rem=0
# i=n
# while(n!=0):
#     rem=n%10
#     sum=sum*10+rem
#     n=n//10
# print("sum = ",sum)
# if(sum==i):
#     print("its pelidrom")
# else:
#     print("its not pelidrom")

# ============find 1 to n num armstrong==================
# i=1
# rem=0
# while(i<=1000):
#         n=i
#         sum=0
#         while(n!=0):
#             rem=n%10
#             sum=sum+(rem*rem*rem)
#             n=n//10
#         if(sum==i):
#             print(i)
#         i=i+1
    
# ============= spy num ===============================
# n=int(input("Enter n = "))
# rem=0
# sum=0
# multi=1
# while(n!=0):
#      rem=n%10
#      sum=sum+rem
#      multi=multi*rem
#      n=n//10
# if(sum==multi):
#     print("its spy no")
# else:
#      print("its not spy no")

# =================== neon num =============================
i=1
rem=0
while(i<=1000):
    n=i
    sum=0
    neon=n*n
    while(neon!=0):
        rem=neon%10
        sum=sum+rem
        neon=neon//10
    if(sum==i):
        print(i)
    i=i+1







