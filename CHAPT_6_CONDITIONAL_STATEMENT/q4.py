 #Write a program to find whether a given username contains less than 10 characters or not.
username = (input("enter your username :"))

if(len(username) < 10):
    print("it contains less than 10 characters")

else:
    print("it has more that 10 characters")