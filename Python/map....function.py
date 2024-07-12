#========== map function in list ====================
# def sum(n):
#     return n+n
# l=[2,4,14,20]
# ans=map(sum,l)
# print(list(l))

# ============== map function in tuple ==============
# def Get(n):
#     return n*n
# l=(20,34,67,54)
# ans=map(Get,l)
# print(tuple(ans))

# ================= map function in set ===========
def Value(n):
    if n%2==0:
        return n
set = {23,43,54,22,88}
ans=map(Value,set)
print(list(ans))

