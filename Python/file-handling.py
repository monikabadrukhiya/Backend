# =========== Read file =================
file=open('python/check.txt','r')
# for i in file:
#     print(i)

# ===================
# files=open('python/check.txt','r')
# date=files.readlines()
# for line in date:
#     word=line.split()
#     print(word)

# ==========read only first 10 character=========
# file=open('python/check.txt','r')
# ans=file.read(10)
# print(ans)

# file.tell() returns the current position of the file pointer after reading.
# file=open('python/check.txt','r')
# pos=file.tell()
# print(pos)

# =========== Write file =======================
# file=open("python/check.txt",'w')
# file.write("ceative design")
# file.write("ceative design")
# file.write("ceative design")
# file.write("ceative design")
# file.write("ceative design")
# file.close()



# =========== Delete file ================
# import os
# os.remove("python/check.txt")


# ======== append the file =============
file=open("python/check.txt","a")
file.write("creative design")
file.close()
