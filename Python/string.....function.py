# ==========find type===============
# str="monika khushal"
# print(type(str))

# slice==============================
# str="hello monika"
# print(str[0:])                                  #hello monika
# print(str[0:5])                                  #hello
# print(str[3:8])                                  #lo mo
# print(str[-1])                                   #a
# print(str[-3:-1])                                #ik
# print(str[-7:-3])                                #mon

# # print reverse string
# print(str[::-1])                                  #akinom olleh

# //////////////////////////////////////////////////////////////////////////////
# 1.capitalize()=it capitalize the first character of the string
# str="monika"
# print(str.capitalize())                       #Monika

# //////////////////////////////////////////////////////////////////////////////
# 2.casefold()===it return a string to lowercase in such case
# str="Creaive Institute"
# print(str.casefold())                         #creative Institute

# ///////////////////////////////////////////////////////////////////////////////
# 3.count()==count char in a string between begin and end index
# str="Creative Institute"
# str2=str.count('e')                  
# print(str2)                                   #2

# str="Creative Institute"
# str2=str.count('e',1,10)
# print(str2)                                   #3

# ////////////////////////////////////////////////////////////////////////////////////
# 4.Endswith()=string terminate with specified char or not returns ture/false
# str="Creative Institute."
# str2=str.endswith('.')
# print(str2)                                    #false

# str="Creative Institute"
# str2=str.endswith('a',1,4)
# print(str2)                 #last pos thi ek pos agal count karine true/false ans ape    

# /////////////////////////////////////////////////////////////////////////////
# 5.find()==it return string between start and end index
# str="Creative Institute "
# str2=str.find("Creative")
# print(str2)                   #0/true
                                #-1/false

# ///////////////////////////////////////////////////////////////////////////////////
# 6.format()==it returns formatted version of set,using the passed value
# str="java "
# str2="python"
# print("{} and {} are programing language".format(str,str2)) 
                            #java  and python are programin language

# str="c# "
# str2="Html"
# print("{0} and {1} are programing language".format(str,str2)) 
                            #c#  and Html are programing language


# ////////////////////////////////////////////////////////////////////////////
# 7.index()= pass string first index can be return
# str="java & pyhton are programing language"
# str1=str.index("ming")
# print(str1)                              #24


# //////////////////////////////////////////////////////////////////////////////
# 8.isalnum=find given string is alphanumeric or not
# alphanumeric=character which is a letter or number is know as alphanumeric
# str="creative123"
# str2=str.isalnum()
# print(str2)

# ///////////////////////////////////////////////////////////////////////////////
# 9.isalpha =check string character are alphabetic or not return true/false
str="creative"
str2=str.isalpha()
print(str2)

# 10.isdecimal =check all the charcer in string are decimal or not return true/false====
# str="123"
# str1="abc"
# str2=str.isdecimal()
# str4=str1.isdecimal()
# print(str2)
# print(str4)

# 11.isdigit()=check all the character in string are digit or not.true/false=====
# str="12345"
# str2=str.isdigit()
# print(str2)

# 12.identifier()= check whether string is a valid identifier or not.true/false=====
# str="creative"
# str2=str.isidentifier()
# print(str2)

# 13.islower()= check given string all character in lowercase or not.true/false
# str="creative"
# str2=str.islower()
# print(str2)

# 14.isnumeric()=check all character of the string are numeric character or not.true/false====
# str="2345"
# str2=str.isnumeric()
# print(str2)

# 15.isupper()= check given string all character in uppercase or not.true/false
# str="ABCDEF"
# str2=str.isupper()
# print(str2)

# 16.join()=is used to concat a string with iterable object,return new string 
# str="/"
# list=["1","2","3"]
# print(str.join(list))

# 17.lower()=convert upper character into lower character
# str="Monika Khushal"
# print(str.lower()) 

# 18.upper()=conver string lower character into upper character
# str="monika barukhiya"
# print(str.upper())

