# 1.abs()===> function is used to return the absolute value of number
# num=abs(3+5j)                          #9+25=34,sqrt(36)
# print(num)                             #5.8

# 2.min(),max()==========================================
# a={2,4,5,8,1}                         # 8
# print(max(a))

# b={23,54,67,12}                       #12
# print(min(b))


# 3.bin()===> is used to return binary representaion of specified integer
# print(bin(20))                         #0b10100


# 4.bool()==>return the boolean of specified object
# x=20
# y=10
# print(bool(x==y))                                #false

# z="cteative Design"
# print(bool(z))                                    #true


# 5.sum()==>is used to get the sum of numbers of an iterable
# s=sum({2,3})
# print(s)                                  #5

# x=sum((1,2,2),10)
# print(x)                                  #15

# y=sum([1+2j,2+3j])
# print(y)                                  #(3+5j)

# z=sum([1+2j,3+4j,2+2])
# print(z)                                  #(8+6j)

# w=sum([1+2j,2,1.5-2j])
# print(w)                                  #(4.5+0j)


# 6.float()==>return a floating point number from number or string
# print(float(8))                           #8.0
# print(float(7.19))                        #7.19
# print(float("-14.23"))                    #-14.23
# print(float("  -17.14\n"))                #-17.14


# 7.format()==>(value,format)

# "b"=>binary format
# print(format(12,"b"))                         #1100

# "C"=>convert value into the unicode character
# print(format(1,"c"))                          #☺

# "d"=>decimal format
# print(format(123,"d"))                        #123

# "e"=>scientific format with lower case e
# print(format(12,"e"))                         #1.200000e+01

# "E"=>scientific format with lower case E
# print(format(123,"E"))                        #1.230000E+02

# "f"=>fix point num format
# print(format(123.456,"f"))                    #123.456000

# "F"=>fix point number format,upper case
# print(format(12.23,"F"))                      #12.230000

# "g"=>general format
# print(format(12,"g"))                         #12

# "G"=>general format using upper case E
# print(format(12,"E"))                         #1.200000E+01

# "o"=>octal format
# print(format(123,"o"))                        #173

# "x"=>hex format,lower case
# print(format(345,"x"))                        #159

# "X"=>hex format,upper case
# print(format(567,"X"))                        #237

# "n"=>number format
# print(format(345,"n"))                        #345


# 8.pow()==>is used to compute power of a number
# print(pow(4,3))                               #64
# print(pow(-4,2))                              #16
# print(pow(4,-2))                              #0.0625
# print(pow(-4,-2))                             #0.0625

# print(pow(4,7,3))                             #((4**7)%3)=(16.384%3)=1

# 9.slice()==>used to get slice of element from the collection of elements
# pyhton provide two overload slice function
# str="creative design"
# a=slice(0,15,3)
# b=slice(-1,0,-3)
# str1=str[a]
# str2=str[b]
# print(str1)
# print(str2)

# 10.divmod()========================================================>
# x=divmod(10,3)
# print(x)                                      #(3,1)

# 11.ord()==return the unicode code of a specified character
# x=ord("h")
# print(x)                                      #104


# 12.round()==>its given roundoff value for a number
# x=round(123.98)
# print(x)                                      #124


# 13.eval()==>fun evalutes the specified expression,if the expression is legal 
# pyhton statment it will be exexuted
# a=2+3-4+(5*6)
# print(a)                                      #31

# 14.sorted()==>
# t=(3,4,8,2,5,8,10)
# print(sorted(t,))                             #[2, 3, 4, 5, 8, 8, 10]



