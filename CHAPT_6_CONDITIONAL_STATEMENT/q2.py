# Write a program to find out whether a student has passed or failed if it requires a total of
#40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
#input from the user.


hindi = int(input("enter the marks you got in exam:"))
english = int(input("enter the marks you got in exam:"))
marathi = int(input("enter the marks you got in exam:"))

precentage = 100 * (hindi + english + marathi)/300

if(precentage>=33 and hindi>=33 and english>=33 and marathi>= 33):
    print("you are paas")

else:
    print("you are fail,try again next time")
