# ==========find type ====================
# days={"mon","tues","thus","wed"}
# print(days)
# print(type(days))

# 1:add()= add item in element=====================
# date={1,4,7,5,2,4}
# date.add(10)
# print(date)                   #{1, 2, 4, 5, 7, 10}

# 2:update()= add item from another set into the current set,join to set element==========
# s={1,2,3}
# s1={11,12,13}
# s.update(s1)
# print(s)                      #{1, 2, 3, 11, 12, 13}
        # iterable list to set using update===========
# s1={11,12,13}
# s2=[100,200]
# s1.update(s2)
# print(s1)             #{100, 200, 11, 12, 13}

# 3.remove(),discard()=to remove item in a set========================
# s={'c','d','m','i'}
# s.remove('d')
# print(s)

            # discard()===================
# s={1,2,3,4}
# s.discard(2)
# print(s)

# 4.pop()=set is use to remove last item,remember that set are unorderd,
# so you will not know what item that gets removed
# s={12,11,1,4,10}
# s.pop()
# print(s) 

# 5.clear()= empties the set=============
# s={3,4,5,6}
# s.clear()
# print(s)              #set{}

# 6.del()=delete the set comletely=========================
# s={2,3,4,5}
# del s
# print(s)              #eror

# set operators//
# pip operators(|)=used to remove dublicate items===================
# d1={"mon","tues","sun","wed","sun"}
# d2={"mon","thus","wed"}
# print(d1|d2)                        #{'wed', 'tues', 'mon', 'thus', 'sun'}   

# 7.union()= that returns a new set containing all items from both sets==========
# d1={"mon","tues","sun","wed","sun"}
# d2={"mon","thus","wed"}
# print(d1.union(d2))                   #{'wed', 'tues', 'mon', 'thus', 'sun'}

# 8.update()=that insert all the items from one set into another=============
# d1={"mon","tues","sun","wed","sun"}
# d2={"mon","tues",'thus'}
# d1.update(d2)
# print(d1)                          #{'tues', 'mon', 'sun', 'wed', 'thus'}

# and & operators//
# and operators(&)= same items can be returns========
# d1={"mon","tues","sun","wed","sun"}
# d2={"mon","thus","wed"}
# print(d1&d2)                                 #{'mon', 'wed'}

# 9.intesection()= it modified the original set by removing the unwanted itemd
# this method return new set =============
# d1={"mon","tues","sun","wed","sun"}
# d2={"mon","thus","wed"}
# print(d1.intersection(d2))                         #{'mon', 'wed'}

# 10.intersection_update()=remove the items from the original set that are not
#  present in both the sets =======
# d1={"mon","tues","sun","wed","sun"}
# d2={"mon","thus","wed"}
# d1.intersection_update(d2)
# print(d1)                                         #{'mon', 'wed'}

# subtraction opretor//
# subtraction opretor(-)=orignal sets remove items presernt in onther set and 
# returns new set
# d={"moni","panvi","keyuri","kinjal"}
# d1={"mohit","khushal","kinjal","moni"}
# print(d-d1)                                  #{'panvi', 'keyuri'}

# 11.difference()= in both set defference item can be return in original set =======
# d={"moni","panvi","keyuri","kinjal"}
# d1={"mohit","khushal","kinjal","moni"}
# print(d.difference(d1))                         # {'panvi', 'keyuri'}

# 12.difference_update()===
# d={"moni","panvi","keyuri","kinjal"}
# d1={"mohit","khushal","kinjal","moni"}
# d.difference_update(d1)
# print(d)                                          #{'panvi','keyuri'}


# 13.symmentric_difference()=it remove that element which is present in both sets==========
# s={"a","b","c"}
# s1={"a",2,3}
# s3=s.symmetric_difference(s1)
# print(s3)                                  #{2, 3, 'b', 'c'}

# 14.symmentric_difference_update()=will keep only the elements that are not 
# present in both sets
# s={"a","b","c"}
# s1={"a",2,3}
# s.symmetric_difference_update(s1)
# print(s)                                         #{'b', 3, 2, 'c'}

# 15.copy()=returns a copy of the set========
# s={1,2,3,4,5}
# s.copy()
# print(s)                    #{1, 2, 3, 4, 5}

#16.isdisjoint()=returns whether two sets have a intersection or not===========
# s={1,2,3,4,5}
# s1={6,7,8}
# print(s.isdisjoint(s1))       #true

# ====false=====
# s={1,2,3,4,5}
# s1={1,2,3}
# print(s.isdisjoint(s1))    #false

# 17.issubset() =returns whether another set contains this set or not=====
# s={1,2,3,4,5}
# s1={11,12,13,14}
# print(s.issubset(s1))   #false

# 17.issuperset() =returns whether this set contains another set or not=====
# s={1,2,3,4,5}
# s1={1,2,3,}
# print(s.issuperset(s1))          #true