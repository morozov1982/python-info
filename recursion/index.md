# Рекурсивные функции

**Рекурсивная функция** - функция, которая вызывает сама себя

Нахождение факториала числа: [factorial.py](factorial.py)
``` Python3
def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n
```

Число из последовательности Фибоначчи: [fibonacci.py](fibonacci.py)
``` Python3
# работает очень медленно, есть более эффективные методы нахождения
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Является ли строка палиндромом (потоп, кабак, шалаш): [palindrome.py](palindrome.py)
``` Python3
def ispalindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return ispalindrome(string[1:-1])
```