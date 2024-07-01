# ============================Inheritance========================================
# 1.single//////////////////////////////////////////////////////////
# class Demo:
#     def First(self):
#         self.a=int(input("Enter a="))
#         self.b=int(input("Enter b="))
# class Demo1(demo):
#     def Second(self):
#         total=self.a+self.b
#         print("total=",total)
# ans=Demo1()
# ans.First()
# ans.Second()

# 2.multilevel/////////////////////////////////////////////////////
# class First:
#     def User(self):
#         self.a=int(input("Enter a="))
#         self.b=int(input("Enter b="))
# class Second(first):
#     def Sum(self):
#         total=self.a+self.b
#         print("total=",total)
# class Third(second):
#     def Div(self):
#         division=self.total//2
#         print("div=",division)
# ans=Third()
# ans.User()
# ans.Sum()
# ans.Div()

# 3.multiple /////////////////////////////////////////////////////
# class first:
#     def list1(self):
#         self.sum=0
#         self.a=[2,4,5,6,8,9]
#         for i in range(len(self.a)):
#             self.sum1=self.sum+self.a[i]
#         print("sum1=",self.sum1)
# class second:
#     def list2(self):
#        self.sum=0
#        self.b=[1,3,7,10,12]
#        for i in range(len(self.b)):
#             self.sum2=self.sum+self.b[i]
#        print("sum2=",self.sum2)

# class third(first,second):
#     def list(self):
#         total=self.sum1+self.sum2
#         print("total=",total)
# ans=third()
# ans.list1()
# ans.list2()
# ans.list()


# 4.herichical///////////////////////////////////////////////////
# class first:
#     def user(self):
#        self.str=input("Enter string=")
# class second(first):
#     def upper(self):
#         upperstr=self.str.upper()
#         print("upperstr=",upperstr)
# class third(first):
#     def lower(self):
#         count=0
#         for i in range(len(self.str)):
#             if(self.str[i]>='a' and self.str[i]<='z'):
#                 count=count+1
#         print("count=",count)

# ans=second()
# ans2=third()
# ans.user()
# ans.upper()
# ans2.user()
# ans2.lower()


# 5.hybrid/////////////////////////////////////////////////////////////////
class first:
    def user(self):
        self.list=[10,34,54,1,24,64,47,86]
class second(first):
    def min(self):
        self.min=self.list[0]
        for i in range(0,len(self.list)):
            if(self.min>self.list[i]):
                self.min=self.list[i]
        print("min value=",self.min)
class third(first):
     def max(self):
        self.max=self.list[0]
        for i in range(0,len(self.list)):
            if(self.max<self.list[i]):
                self.max=self.list[i]
        print("max value=",self.max)
class forth(second,third):
    def sum(self):
        sum=self.min+self.max
        print("sum=",sum)

ans=forth()
ans.user()
ans.min()
ans.max()
ans.sum()









