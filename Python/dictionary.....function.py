# ============find keys,values,items=================
# a={"name":"monika","age":12}
# print(type(a))

# ===============get all keys==============================
# print(a.keys())

# =============get all values============================
# print(a.values())

# ==================get all items====================
# print(a.items())


# =========Eter 1 key and add miltiple values===================
# n=int(input("Enter n="))
# value=[]
# for i in range(n):
#    name= input("Enter Email=")
#    value.append(name)
# print(value)
# data={"name":value}
# print(data)

# s1=dict({"name":"moni","course":"python","time":10})
# print(s1)

# s1=dict([("name","moni"),("course","python"),("time",10)])
# print(s1)

# iterating a dictionary////////////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# for i in s1:
#     print(i,s1[i])

# 1.get()/////////////////////////////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# print(s1["name"])
# print(s1.get(''))


# 2.items()///////////////////////////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10-12}
# for i in s1.items():
#     print(i[0])

# s1={"name":"moni","course":"python","time":10-12}
# for i in s1.items():
#     print(i[0],i[1])


# 3.update()////////////////////////////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# s1['fees']=40000
# s1.update({"job":"yes"})
# print(s1)

        # pass new key as list of tuple///////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# s1.update([("weight",55),("height",5.3)])
# print(s1)

        # update the state using update()////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# s1.update({"state":"raj"})
# for i,j in s1.items():
#     print(i,":",j)


# Removing item from the dictionary///////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10}

# 1.pop()==
# s1.pop('name')
# print(s1)

# 2.popitem()==
# s1.popitem()
# print(s1)

# 3.del key==
# del s1['time']
# print(s1)

# 4.clear()==
# s1.clear()
# print(s1)

# 5.del==
# del s1


# checking if a key exists///////////////////////////////////////////////////
# keys() method ============================
# s1={"name":"moni","course":"python","time":10}
# keyname="pass"
# if keyname in s1.keys():
#     print("name is",s1[keyname])
# else:
#     print("key not found")


# join two dictionary////////////////////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# s2={"fess":23000,"result":"pass"}
# s1.update(s2)
# print(s1)

                # useing  **kwargs==============
# s1={"name":"moni"}
# s2={"num":12345}
# s3={"course":"python"}
# s={**s1,**s2,**s3}
# print(s)
 
        # two join dict few item in common==============
# s1={"name":"moni","course":"python","time":10}
# s2={"fess":23000,"time":10}
# s1.update(s2)
# print(s1)

# copy()/////////////////////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# s2=s1.copy()
# print(s2)

# sort dictionary//////////////////////////////////////////////////////
# s1={"name":"moni","course":"python","time":10}
# print(sorted(s1.items()))
# print(sorted(s1.keys()))

s1={"name":50,"course":20,"time":10}
print(sorted(s1.values()))

