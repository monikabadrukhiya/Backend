# ================ sum value =========
# def sum(n,m):
#     return n+m

# ==============pelidrome===================
# def Peli(n):
#     sum=0
#     rem=0
#     while(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
#     return sum

# ============= armstrong =================
def Arm(n):
    sum=0
    while(n!=0):
        rem=n%10
        sum=sum+(rem*rem*rem)
        n=n//10
    return sum