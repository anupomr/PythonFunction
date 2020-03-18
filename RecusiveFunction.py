# Binary Search
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


info = [2, 3, 4, 5, 7, 8, 9, 12, 14, 16, 17, 28]

print(binary_search(info, 9, 1, 12))


# Multiplication in recursive
def multiplication(multiplier, multiplicand):
    if multiplicand == 1:
        return multiplier
    else:
        return multiplier + multiplication(multiplier, multiplicand - 1)


print(multiplication(5, 4))


# Recursive product
def power(num, k):
    if k == 1:
        return num
    else:
        return num * power(num, k - 1)


print(power(5, 5))


# Recursive Fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Test Fibonacci sequence
for j in range(4):
    print(fibonacci(j), ", ", end=' ', flush=True),
