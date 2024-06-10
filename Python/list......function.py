list=[10,40,35,67,89,54,35,97]
# print(min(list))
# print(max(list))
# print(sum(list))
# print(len(list))

#  append : Add an item to the end of the list. ========================
# a=[23,65,78,98,23,47,76]
# b=[100]
# a.append(b)
# print(a)
        # full array add in last======
# a=[23,65,78,98,23,47,76]
# b=[100,200,300,400,500]
# a.append(b)
# print(a)

# extend :Extend the list by appending all the items from the iterable============
# a=[23,65,78,98,23,47,76]
# b=[100,200,300,400,500]
# a.extend(b)
# print(a)

# insert :Insert an item at a given position. The first argument is the index  of the
#  element before which to insert, so  inserts at the front of the list, 
# a=[45,76,68,98,90,34,12]
# a.insert(2,100)
# print(a)

# remove :Remove the first item from the list whose value is equal to list
# direct add value
# a=[23,65,67,98,45,100,33]
# a.remove(100)
# print(a)

#  pop :Remove the item at the given position in the list, and return it. 
# If no index is specified, removes and returns the last item in the list.
# a=[44,55,66,88,100,40]
# (a.pop(len(a)-1))
# print(a)

# index :return pass value index
# a=[22,54,65,67,87]
# print(a.index(65))

# count :Return the number of times value appears in the list.
# a=[23,65,78,98,23,47,76,23]
# print(a.count(23))

# sort : list gives in accending order
# a=[23,65,78,98,15,47,76,2]
# a.sort()
# print(a)

# Reverse :Reverse the elements of the list in place.
# a=[23,65,78,98,15,47,76,2]
# a.reverse()
# print(a)

# Copy: Return a shallow copy of the list.
# a=[23,65,78,98,15,47,76,2]
# a.copy()
# print(a)

# ============== list in descending order===========
a=[45,56,87,90,100,23,15,10]
a.sort(reverse=True)
print(a)

b=[45,56,87,90,100,23,15,10]
b.sort(reverse=False)
print(b)


