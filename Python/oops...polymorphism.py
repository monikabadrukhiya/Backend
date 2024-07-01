# ================Funoveriding/Run-time Function===============================
class First:
    def value(self):
        self.n=int(input("Enter n="))
class Second(First):
    def Sum(self):
     super().value()
     self.sum=0
     rem=0
     while(self.n!=0):
         rem=self.n%10
         self.sum=self.sum*10+rem
         self.n=self.n//10
     print("sum==",self.sum)
class Third(Second):
    def Get(self):
       super().Sum()
       super().value()
       print("s=",self.sum)
       print("n=",self.n)

       if(self.sum==self.n):
            print("code Execute succesfully")
ans=Third()
ans.Get()

         
