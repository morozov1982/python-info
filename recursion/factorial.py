def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


if __name__ == '__main__':
    print(factorial(4))
    print(factorial(10))
