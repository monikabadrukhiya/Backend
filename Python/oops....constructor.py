# ======================Constructor==============================
class First:
   def __init__(self):
      print("Good Morning")
c=First()

# ================================================================
class First:
    def __init__(self,a,b):
        self.a= a+b

    def Value(self):
        return("division=",self.a)
ans=First(20,10)
print(ans.Value())


# =========================multiplication ====================
class First:
    def __init__(self):
        self.a=int(input("Enter a="))
        self.b=int(input("Enter b="))
class Second(First):
    def Multi(self):
        self.multi=self.a*self.b
        print("multi==",self.multi)
ans=Second()
ans.Multi()

