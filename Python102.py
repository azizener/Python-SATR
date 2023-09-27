import datetime

name1 = "khalid"
date1 = datetime.date(1989,2,1)
name2 = "Nouf"
date2 = datetime.date(2004,9,2)
name3 = "khalid"
date3 = datetime.date(2009,12,9)
age1 = 2021-date1.year
day1 = date1.strftime("%A")
print(name1 + " is " + str(age1) + " years old and he/she was born on " + day1)
age2 = 2021-date2.year
day2 = date2.strftime("%A")
print(name2 + " is " + str(age2) + " years old and he/she was born on " + day2)
age3 = 2021-date3.year
day3 = date3.strftime("%A")
print(name3 + " is " + str(age3) + " years old and he/she was born on " + day3)

ages = [age1, age2, age3]

Max = max(ages)
Min = min(ages)

if Max == age1:
    print("The oldest one is "+ str(age1))
elif Max == age2:
    print("The oldest one is " + str(age2))
else:
    print("The oldest one is " + str(age3))

if Min == age1:
    print("The youngest one " + str(age1))
elif Min == age2:
    print("The youngest one " + str(age2))
else:
    print("The youngest one " + str(age3))

print("Total People: " + str(len(ages)))