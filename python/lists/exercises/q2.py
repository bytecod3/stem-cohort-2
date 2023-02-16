from random import randint

# create an empty list
nums = []

# a) create the list
# fill the list with empty values
for i in range(20):
    # generate a random number
    n = randint(0, 100)

    # append to the list
    nums.append(n)

#b) print the list
# print the list
for num in nums:
    print(num)

#c) find the average of a list
# find the aerage of the list
for num in nums:
    total += num

# average =  total/ no.of items
avg = total / len(nums)

print(avg)

# c) print the largest value
nums.max()

# d) print the smallest
nums.min()

# d) second largest and second smallest -  you have to sort the list
nums.sort()

# second largest
nums[1]

# second smallest 
nums[len(nums) - 1]

# e) number of even values
for num in nums:
    # check whether it is even using the modulo operator
    if num % 2 == 0:
        count += 1
    
# count now contains number of even values ion the list
print(count)