# -*- coding: utf-8 -*-

while True:
    try:
        x=int(raw_input("Enter a number between 1 and 9: "))
        break
    except:
        print "It is not a number... Try again..."

if 1<=x<4:
    print x
    s=raw_input("Enter a string: ")
    n=int(raw_input("Enter repetition times: "))
    while n>0:
        print s
        n-=1

elif 4<=x<7:
    m=int(raw_input("Enter Power degree: "))
    print x**m

elif 7<=x<10:
    count=10
    while count>0:
        x+=1
        count -=1
        print x
else:
    print "Number is out of specified range... Quiting the programm..."
