#A spam comment is defined as a text containing following keywords: “Make a lot of
#money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams
 
post = input("enter your post :")
message1 = "make a lot of money"
message2 = "buy now"
message3 = "subscribe this"
message4 = " click this"


if(message1 in post or message2 in post or message3 in post or message4 in post):
    print("this is spam , dont believe in this")
else:
    print("this  is not spam")


