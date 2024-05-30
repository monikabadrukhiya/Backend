# ==========find odd even=================
# n=124
# print("n=",n)
# a=n%10
# print("last digit=",a)

# b=n//10
# print("first two digit=",b)

# c=b%10
# print("last digit=",c)

# if c%2==0:
#     print("its even number")
# else:
#     print("its even number")

# ==========find positive value==========

# n=int(input("Enter number="))
# if n>=0:
#     print("this is positive num")
# else:
#     print("this is negarive value")

# ============== find odd even number==========
# n=int(input("Enter num="))
# if n%2==0:
#     print("its even num")
# else:
#     print("its odd num")


# ==================== find max value=============
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))

# if a>b:
#     if a>c:
#         if a>d:
#             print("a is max")
#         else:
#             print("d is max")
#     elif c>d:
#         print("c is max")
#     else:
#         print("d is max")
# elif b>c:
#     if b>d:
#         print("b is max")
#     else:
#         print("d is max")
# elif c>d:
#     print("c is max")
# else:
#     print("d is max")

#================= ledder if find min value=========
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=int(input("d="))

# if(a<b and a<c and a<d ):
#     print("a is min")
# elif(b<c and b<d):
#     print("b is min")
# elif  c<d:
#     print("c is min")
# else:
#     print("d is min")
    

# ===========find equal value==========
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))

# if a==b:
#     if a==c:
#         print("a,b,c are same")
#     else:
#         print("a,b are same but c id different")
# elif b==c:
#     print("b,c is ssame but a is diff")
# elif a==c:
#     print("a,c are same")
# else:
#     print("all are diff")

# ==========result=======================
a=int(input("science = "))
b=int(input("english = "))
c=int(input("hindi = "))
d=int(input("ss = "))
e=int(input("maths = "))

if(a>=33 and b>=33 and c>=33 and d>=33 and e>=33):

    # === total marks
    total=a+b+c+d+e
    print("total=",total)
    # ===total per====
    per=total/5
    print ("per = ",per)

    # ===find grade====
    if(per>90):
        print(" A Grade")
    elif per>=80:
        print("B Grade")
    elif per>=70:
        print("C Grade")
    elif per>=60:
        print("D Grade")
    else:
        print("E Grade")

    # ===find maximum marks====
    if(a>b and a>c and a>d and a>e):
        print("science is max =",a)
    elif( b>c and b>d and b>e ):
        print("english is max = ",b)
    elif(c>d and c>e):
        print("hindi is max=",c)
    elif(d>e):
        print("ss is max=",d)
    else:
        print("maths is max =",e)
        
    # ===minimum marks===
    if(a<b and a<c and a<d and a<e):
        print("science is min =",a)
    elif( b<c and b<d and b<e ):
        print("english is min = ",b)
    elif(c<d and c<e):
        print("hindi is min=",c)
    elif(d<e):
        print("ss is min=",d)
    else:
        print("maths is main=",e)
else:
    print("Fail")




    


