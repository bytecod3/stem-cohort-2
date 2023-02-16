# my first python list
numbers = [45, 67, 34, 90]
names = ["python", "c++", "java", "typescript"]

print(len(numbers)) # get the length on my list

for i in range(len(numbers)):
    print(numbers[i])

# LIST METHODS
# Index - gets the index of an element in a list
print(numbers.index(76))
print(names.index("typescript"))

# APPEND - adds an element to the end of a list

# before appending
for i in range(len(numbers)):
    print(numbers[i])

print("\n")
numbers.append(90)

# after appending
for i in range(len(numbers)):
    print(numbers[i])

# SORT - arranges the list in ascending order
# sort the list
numbers.sort() 

# add a new line for formatted output
print("\n")

# COUNT - returns the number of times an
# element occurs in a list
print(numbers.count(67))

# POP - removes an element at a given index
# and returns that element
print(numbers.pop(2))

# INSERT - inserts an element x at an index y
numbers.insert(2, 100)

for i in range(len(numbers)):
    print(numbers[i])

# REMOVE - removes the first occurence of an
# element from the list
numbers.remove(67)

# TIPS AND TRICKS

# multiplying a list
zeros = [0]*10

# # adding two lists
list1 = [89, 90]
list2 = [45, 66]
final_list = list1 + list2

# # Slicing a list
nums = [12, 13, 34, 65, 23, 54]

# # get the maximum value in a list
max(nums)

# # get the minimum value
min(nums)

# creating lists
nums = [] # empty list

for i in range(10):
    # insert elements into the list
    nums.append(i)

for i in range(len(nums)):
    print(nums[i])

# EXERCISES
#  create a list of even numbers
even_nums = []

for num in range(20):
    if(num % 2 == 0):
        even_nums.append(num)

for i in even_nums:
    print(even_nums[i])
