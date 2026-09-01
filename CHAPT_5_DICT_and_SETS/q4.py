#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
#use key as their names. Assume that the names are unique
dict={}
f1 = input("enter your name:")
l1 = input("enter  your favourite language:")
dict.update({f1:l1})
f2 = input("enter your name:")
l2 = input("enter  your favourite language:")
dict.update({f2:l2})
f3 = input("enter your name:")
l3 = input("enter  your favourite language:")
dict.update({f3:l3})
f4 = input("enter your name:")
l4 = input("enter  your favourite language:")
dict.update({f4:l4})

print(dict)
