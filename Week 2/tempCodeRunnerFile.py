#Task 1
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(10, 20, 30))

#Task 2
def reverse_string(s):
    return s[::-1]

sample_string = "1234abcd"
print(reverse_string(sample_string))

#Task 3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(7))
