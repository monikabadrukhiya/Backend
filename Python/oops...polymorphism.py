# ================Funoveriding/Run-time Function===============================
# class First:
#     def value(self):
#         self.n=int(input("Enter n="))
# class Second(First):
#     def Value(self):
#      super().value()
#      self.i=self.n
#      self.sum=0
#      rem=0
#      while(self.n!=0):
#          rem=self.n%10
#          self.sum=self.sum*10+rem
#          self.n=self.n//10
#      print("sum==",self.sum)
#      if(self.sum==self.i):
#             print("code Execute succesfully")
# ans=Second()
# ans.Value()

# ================================================================================
class First:
    def User(self):
        self.i = int(input("Enter n="))
class Second(First):
    def User(self):
        super().User() 
        while(self.i<=1000):
            self.n=self.i
            self.sum=0
            rem=0
            while(self.n!=0):
                rem=self.n%10
                self.sum=self.sum+(rem*rem*rem)
                self.n=self.n//10
                if(self.sum==self.i):
                    print("value=",self.sum)
            self.i=self.i+1
ans=Second()
ans.User()
         
