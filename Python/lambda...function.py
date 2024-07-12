a=lambda s:12+s
print(a(12))

ans=lambda a,b:a+b
print(ans(12,24))


# =====================odd/ even================
ans=lambda s:s%2
a=int(input("Enter no="))
if(ans(a)==0):
    print("its even")
else:
    print("its odd")

# in list ==============================================
list=[12,32,34,54]
list1=lambda s:list.append(s)
list1(100)
print(list)