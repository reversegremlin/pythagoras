# R-1.1
# Write a short Python function, is multiple(n, m), that takes two integer values and returns
# True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def is_multiple(m, n):
    return True if m % n == 0 else False


print(is_multiple(10, 3))
print(is_multiple(10, 2))

# R-1.2
# Write a short Python function, is even(k), that takes an integer value and returns True if k is even,
# and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return False if k & 1 else True


print(is_even(2))
print(is_even(3))

# R-1.3
#Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest


alpha = [7, 2, 3, 4, 5, 6, 7, 8, 99]

print(minmax(alpha))


# R-1.4
# Write a short Python function that takes a positive integer n and returns the sum of the squares
#  of all the positive integers smaller than n.


def sum_of_squares(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total


print('sum of squares')
print(sum_of_squares(4))

# R-1.5
# give a single command that computes the sum from exercise r-1.4, relying on python's comprehension syntax and built in sum function

def sum_of_squares2(n):
    return sum([k * k for k in range(0, n)])


print(sum_of_squares2(4))

# R-1.6
#Write a short Python function that takes a positive integer n and returns the sum of the squares
# of all the odd positive integers smaller than n.


def sum_of_squares_odd(n):
    n -= 1
    total = 0
    while n > 0:
        if n % 2 != 0:
            total += n * n
        n -= 1
    return total


print('sum of squares odd')
print(sum_of_squares_odd(4))
# R-1.7

# give a single command that computes the sum from r-1.6, relying on python's comprehension syntax and built in sum function



def sum_of_squares_odd2(n):
    return sum([k * k for k in range(0, n) if k % 2 != 0])


print(sum_of_squares_odd2(4))


# R-1.8
# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used
# for index -n <= k < 0, what is the equivalent index j >= 0 such that s[j]
# references the same element?

s = "pythonstring"
k = -1
print(s[k])
n = len(s)
print(s[n + k])
print


for j in range(-n, 0):
    print(s[j])


for j in range(-n, 0):
    print(s[j + n])


# print(s[0])

# R-1.9


# R-1.10


# R-1.11


# R-1.12



