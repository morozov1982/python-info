# работает очень медленно, есть более эффективные методы нахождения
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # 0 1 1 2
    print(fibonacci(5))  # 3
    print(fibonacci(6))  # 5
    print(fibonacci(7))  # 8
    print(fibonacci(8))  # 13
    print(fibonacci(9))  # 21
    print(fibonacci(10))  # 34
