
num = eval(input("Enter a number: ")) # ask the user for input

# check if the input is a negative number
if num < 0: 
    print("Wrong input")

# if it is a positive number divide it by 2
else:
    if num > 50:
        x = num/2

        # print the divided value
        print(x) 
    else:
        print("Number is less than 50")


# program to check is a user input is less than 15
temp = eval(input("Enter a number: ")) # ask the user for input
if temp < 15:
    print("Input is less than 15")
else:
    print("Input is greater than 15")


# program to print a simple pattern
for i in range(6):
    print("*" * i)

# program to print numbers starting from 10 to 0
for i in range(10, 0, -1):
    print(i)
