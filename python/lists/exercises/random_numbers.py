from random import randint

nums = []

# generate a list of random numbers
for i in range(20):
    number = randint(1, 100)
    nums.append(number)

for x in nums:
    print(x)


# Get the number of even numbers in a list
# nums = [67, 879, 90, 56, 44, 59]

# count = 0
# for num in nums:
#     if num % 2 == 0:
#         count = count + 1
    
# print(count)



