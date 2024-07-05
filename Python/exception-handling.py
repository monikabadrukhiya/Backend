# ============== sum of two elements =============
a=10
b="20"
try:
    sum=a+b
    print("a=",sum)
except:
    print("error")


# =================== pelidrome num =========================
def spy(i):
    sum=0
    multi=1
    while(i!=0):
        rem=i%10
        sum=sum+rem
        multi=multi*rem
        i=i//10
    return(sum==multi)
i=int(input("Enter n="))
ans=(spy(i))
def check (ans,i):
    if ans==1:
        print("its spy no")
    else:
        print("its not spy no")
check(ans,i)
try:
    spy()
except:
    print("check code")
