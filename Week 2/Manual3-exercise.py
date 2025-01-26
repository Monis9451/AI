#Task 1
dictionary = {
    'three': 3,
    'one': 1, 
    'two': 2,
    'four': 4
    }

ascending = dict(sorted(dictionary.items(), key=lambda item: item[1]))
descending = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)

#Task 2
# Write a Python script to check if a given key already exists in a dictionary.

dictionary2 = {
    'one': 1, 
    'two': 2,
    'three': 3,
    'four': 4
    }
key = 'two'

if key in dictionary:
    print(f"{key} exists in the dictionary")
else:
    print(f"{key} does not exist in the dictionary")

#Task 3
# Write a Python script to merge two Python dictionaries.

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
merge = {**dict1, **dict2}
print(merge)

#Task 4
#Write a Python program to add an item in a tuple.
tup = (1, 2, 3)
item = (4,)
tup += item
print(tup)

#Task 5
# Write a Python program to create a tuple with different data types
tup2 = (1, 'two', 3.0)
print(tup2)

#Task 6
# Write a Python program to sum all the items in a list
list1 = [1, 2, 3, 4]
sum = 0
for i in list1:
    sum += i
print(sum)

#Task 7
# Write a Python program to get the largest number from a list.
list2 = [1, 2, 3, 4]
print(max(list2))

#Task 8
# Write a Python program to add member(s) in a set.
set1 = {1, 2, 3}
set1.add(4)
print(set1)

#Task 9
# Write a Python program to reverse the order of the items in the array
array = [1, 2, 3, 4, 5]
array.reverse()
print(array)

#Task 10
# Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.
array = [1, 2, 3, 4, 5]
print(array)
print(f"This is 0th index: {array[0]}")
print(f"This is 1st index: {array[1]}")
print(f"This is 2nd index: {array[2]}")
print(f"This is 3rd index: {array[3]}")
print(f"This is 4th index: {array[4]}")

