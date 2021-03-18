num1 = input("Enter first Number:  ")
num2 = input("Enter second Number:  ")
num3 = input("Enter third Number:  ")

if (num1 > num2) and (num1 > num3):
    print("The highest number is: "+num1)
elif (num2 > num1) and (num2 > num3):
    print("The highest number is: " + num2)
else:
    print("The highest number is: " + num3)
