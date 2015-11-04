print "Society in XXI Century"
while True:
    try:
        age=int(raw_input("What's your age?: "))
        break
    except:
        print "It is not a number... Try again..."

if 0<age<7:
    print "You gotta go to children garden"

elif 7<=age<18:
    print "High school"

elif 18<=age<25:
    print "University"

elif 25<=age<60:
    print "Work"

elif 60<=age<121:
    print "Now you can live your life"

else:
    count =5
    while count>0:
        count -=1
        print "Error! This programm is for human only"

