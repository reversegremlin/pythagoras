# Write a short Python function, is multiple(n, m), that takes two integer values and returns
# True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def is_multiple(m, n):
    return True if m % n == 0 else False


print(is_multiple(10, 3))
print(is_multiple(10, 2))

# Write a short Python function, is even(k), that takes an integer value and returns True if k is even,
# and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(k):
    return False if k & 1 else True


print(is_even(2))
print(is_even(3))


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
#
# Write a short Python function that takes a positive integer n and returns the sum of the squares
#  of all the positive integers smaller than n.


def sum_of_squares(n):
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total


print(sum_of_squares(3))


def sum_of_squares2(n):
    return sum([k * k for k in range(0, n + 1)])


print(sum_of_squares2(3))

#Write a short Python function that takes a positive integer n and returns the sum of the squares
# of all the odd positive integers smaller than n.


def sum_squares_odd(n):
    total = 0
    while n > 0:
        if is_even(n):
            total += n * n
            n -= 1
    return total
