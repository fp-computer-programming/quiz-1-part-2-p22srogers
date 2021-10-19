# Author: SMR (AMDG) 10/19/21
year=int(input("What is the Year of the Date? "))
month=int(input("What is the Month of the date? "))
day=int(input("What is the Day of the Date? "))
j=year//100
k=year%100
m=month
q=day
if month ==1:
    m=m+11
if month ==2:
    m=m+12
h=(q + (((26*(m+1))//10))+k+(k//4)+(j//4)+(5*(j)))%7

if h==0:
    print("The Day of the Week is Saturday. ")
elif h==1:
    print("The Day of the Week is Sunday. ")
elif h==2:
    print("The Day of the Week is Monday. ")
elif h==3:
    print("The Day of the Week is Tuesday. ")
elif h==4:
    print("The Day of the Week is Wednesday. ")
elif h==5:
    print("The day of the Week is Thursday. ")
else:
    print("The Day of the Week is Friday. ")


