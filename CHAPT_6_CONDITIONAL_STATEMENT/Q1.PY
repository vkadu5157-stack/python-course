# Write a program to find the greatest of four numbers entered by the user

num1 = int(input("enter first number:"))
num2 = int(input("enter first number:"))
num3 = int(input("enter first number:"))
num4 = int(input("enter first number:"))

if(num1>num2 and num1>num3 and num1>num4):
    print("num1 is the greatst among four numbers",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("num2 is the greatst among four numbers",num2)
elif(num3>num2 and num3>num1 and num3>num4):
    print("num3 is the greatst among four numbers",num3)
elif(num4>num1 and num4>num2 and num4>num3):
    print("num4 is the greatst among four numbers",num4)
else :
    print("programme is over")

