# =====================reverse value and check same or not==================
# method:1
# def rev(n):
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
#     return(sum)
# n=int(input("Enter value="))
# c=rev(n)
# print(c)
# def check(c,n):
#     if(c==n):
#         print("yes")
#     else:
#         print("no")
# print=check(c,n)

# =====================method:2==================
# def rev(n):
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum=sum*10+rem
#         n=n//10
#     return(sum)
# n=int(input("Enter no="))
# c=rev(n)
# print("reverse value=",c)

# def check(n,c):
#     return n==c
# k=check(n,c)
# if(k==1):
#     print("both are same")
# else:
#     print("different")

# ===================spy number====================
# def spy(n):
#     sum=0
#     multi=1
#     while(n!=0):
#         rem=n%10
#         sum=sum+rem
#         multi=multi*rem
#         n=n//10
#     return(sum==multi)    
# n=int(input("Enter no="))
# s=spy(n)
# # print("spy",s)
# def check(s,n):   
#     if(s==1):
#         print("spy no")
#     else:
#         print("not spy num")
# check(s,n)

        # ==========  method : 2  ========================
# def sum(n):
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum=sum+rem
#         n=n//10
#     return(sum)
# def multi(n):
#     multi=1
#     while(n!=0):
#         rem=n%10
#         multi=multi*rem
#         n=n//10
#     return(multi)
# n=int(input("Enter no="))
# a=sum(n)
# b=multi(n)
# print("sum=",a)
# print("multi=",b)

# def check(a,b):
#     if(a==b):
#         print("its spy num")
#     else:
#         print("its not spy num")
# check(a,b)

# ====================  armstrong num===============================
# def arm(n):
#     sum=0
#     while(n!=0):
#         rem=n%10
#         sum=sum+(rem*rem*rem)
#         n=n//10
#     return(sum)
# n=int(input("Enter no="))
# k=arm(n)
# print("return value",k)

# def check(k,n):
#     if(k==n):
#         print("its armstrong no")
#     else:
#         print("its not armstrong num")
# check(n,k)


# ========================== neon num=================================
# def neon(n):
#     m=n*n
#     sum=0
#     while(m!=0):
#         rem=m%10
#         sum=sum+rem
#         m=m//10
#     return(sum)
# n=int(input("Enter no="))
# k=neon(n)
# print("Return no=",k)

# def check(n,k):
#     if(n==k):
#         print("its neon num")
#     else:
#         print("its not neon num")
# check(n,k)


# =================  nested function===================
# def first():
#     print("keval")
#     def second():
#         print("mansi")
#         def third():
#             print("panvi")
#             def forth():
#                 print("khushal")
#                 def fifth():
#                      print("moni")
#                 return fifth()
#             return forth()
#         return third()
#     return second()
# first()

# =============================fun call another function=====================
# def first():
#     print("hii")
# def second():
#     print("hello")
# def third():
#     print("wel come")
# def forth():
#     print("Bye")
# def fifth():
#     first()
#     second()
#     third()
#     forth()
#     print("moni khushal")
# fifth()


# =============check given num ================================
# pelidrom
# armstrong
# neon
# spy

def peli(i):
    sum=0
    n=i
    while(n!=0):
         rem1=n%10
         sum=sum*10+rem1
         n=n//10
    return (sum==i)

def arm(i):
     n=i
     rev=0
     while(n!=0):
         rem2=n%10
         rev=rev+(rem2*rem2*rem2)
         n=n//10
     return( rev==i)

def spy(i):
     sum1=0
     multi=1
     n=i
     while(n!=0):
        rem=n%10
        sum1=sum1+rem
        multi=rem*multi
        n = n//10      
     return(sum1==multi)

def neon (i):
    n=i*i
    neon=0
    while(n!=0):
        rem=n%10
        neon=neon+rem
        n=n//10
    return(neon==i)

i=int(input("Enter num ="))
pelival=peli(i)
print("pelidrom value =",pelival)

armval=arm(i)
print("armstrong value =",armval)

spyval=spy(i)
print("spy value =",spyval)

neonval=neon(i)
print("neon value =",neonval)

def input(pelival,armval,spyval,neonval):
    if(pelival==1 and armval==1 and spyval==1 and neonval==1 ):
         print("its pelidrom ,armstrong ,spy, neon num")
    elif(pelival==1 and armval==1 and spyval==1):
        print("its pelidrom, armstrong, spy num")
    elif(pelival==1 and armval==1 and neonval==1):
        print("its pelidrom, armstrong, neon num")
    elif(pelival==1 and spyval==1 and neonval==1):
        print("its pelidrom, spy, neon num")
    elif(armval==1 and spyval==1  and neonval==1):
        print("its  armstrong, spy, neon num")
    elif(pelival==1 and armval==1):
        print("its pelidrom, armstrong num")
    elif(pelival==1 and  spyval==1):
        print("its pelidrom,  spy num")
    elif(pelival==1 and neonval==1):
        print("its pelidrom,neon num")
    elif(armval==1 and spyval==1):
        print("its armstrong, spy num")
    elif(armval==1  and neonval==1):
        print("its armstrong, neon num") 
    elif(spyval==1 and neonval==1):
        print("its spy, neon num")
    elif(pelival==1):
        print("its pelidrom num")
    elif(armval==1):
        print("its armstrong num")
    elif(spyval==1):
        print("its spy num")
    elif(neonval==1):
        print("its neon num")
    else:
        print("non of this")
input(pelival,armval,spyval,neonval)

