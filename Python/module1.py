import module
# ==============sum value ========================
# print(module.sum(23,45))

# =========pelidrom num========================
# n=int(input("Enter n="))
# print(module.Peli(n))

# ========== armstring  num ==================
n=int(input("Enter n="))
ans=(module.Arm(n))
if ans==n:
    print("its armstrong")
else:
    print("its not armstrog")