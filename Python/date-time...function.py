import datetime as dt
# ====datetime.now()======================
d=dt.datetime.now()
print("current date time==",d)

# ======date()=========================
# x=d.date()
# print("date=",x)


# ====time()===============================
# y=d.time()
# print("time=",y)

# ========================strftime()=============================
# convert to date string========>
# date=d.strftime("%d/%m/%y")
# print("date string =",date)

# convert to time string========>
# time=d.strftime("%H:%M:%S")
# print(time)

# %d==>return the day of the month ,from 1 to 31
# day=d.strftime("%d")
# print("day=",day)

# %m==>return the month of the year ,from 1 to 12
# month=d.strftime("%m")
# print(month)

# %y==>return the year in two digit ,like:19,20,21
# year=d.strftime("%y")
# print(year)

# %Y==>return the year in four digit ,like:2024
# year=d.strftime("%Y")
# print(year)

# %A==>return the full name of the weekday,    ex:monday
# wday=d.strftime("%A")
# print(wday)

# #a==>return the short name of the weekday, wx:mon
# wday=d.strftime("%a")
# print(wday)

# %B==>return the full name of the month, ex:july
# month=d.strftime("%B")
# print(month)

# %b==>return the short name of the month, ex:apr
# month=d.strftime("%b")
# print(month)

# %H==>return the hour in 24 hr format
# hour=d.strftime("%H")
# print(hour)

# %I==>return the hour in 12 hr formtat
# hout=d.strftime("%I")
# print(hour)

# %M==>return the minutes from 00 to 59
# min=d.strftime("%M")
# print(min)

# %S==>return the second from 00 to 59
# sec=d.strftime("%S")
# print(sec)

# %f==>return the microsconds
# microsec=d.strftime("%f")
# print(microsec)

# %p==>return time in AM/PM format
# pm=d.strftime("%p")
# print(pm)

# %c==>return local's appropriate date time
# ldatetime=d.strftime("%c")
# print(ldatetime)                                  #Thu Jul  4 10:32:14 2024

# %x==>return local's appropriate date
# ldate=d.strftime("%x")
# print(ldate)                                      #07/04/24

# %X==>return local's appropriate time
# ltime=d.strftime("%X")
# print(ltime)                                      #10:34:52

# %z==>return the UTC offset(empty string if the object is naive)
# day=d.strftime("%z")
# print(day)

# %Z==>return time zone name(empty string if the object is naive)
# day=d.strftime("%Z")
# print(day)

# %j==>return the day of the year from 01 to 366
# dyear=d.strftime("%j")
# print(dyear)                                  

# %w==>return weekday as a decimal number,where 0 is sunday and 6 is suturday
# weekday=d.strftime("%w")
# print(weekday)

# %U==>return the week number of the year(sunday as the first day of the year)
# wyear=d.strftime("%U")
# print(wyear)

# %W==>return the week number of the year(monday as the first day of the year)
# wyear=d.strftime("%W")
# print(wyear)

# %H:%M:%S==>24 hour format==>
# print("24 hr format== ",d.strftime("%H,%M,%S"))
# print("12 hr format==",d.strftime("%I-%M-%S"))


