# ask the user for input
list_length = eval(input("What is your desired list length? "))

nums = []

for i in range(list_length):
    # prompt user to enter a list of numbers
    num = eval(input("Enter number: "))

    # if the user enters a number greater than 12, tell them its wrong and allow them to re-enter the number
    while num > 12:
        print("Error: number must be between 1 and 12")
        num = eval(input("Enter number: "))
   
    # append correct to list
    nums.append(num)

# print the list
for num in nums:
    print(num)

print("\n")

# replace all numbers greater than 10 with 10 using the insert method
for num in nums:
    if num > 10:
        # get the index of the number greater than 10
        nums.index(num)

        # replace the number with 10
        nums.insert(nums.index(num))

    
# print the new list
for num in nums:
    print(num)
