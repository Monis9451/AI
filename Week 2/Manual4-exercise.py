#Task 1
# Write a Python function to find the Max of three numbers.
def max_of_three(a, b, c):
    return max(a, b, c)
print(max_of_three(7, 9, 3))

#Task 2
# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
string = "1234abcd"
print(string[::-1])

#Task 3
# Write a Python function to calculate the factorial of a number (a non-
# negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = 5
print(factorial(n))