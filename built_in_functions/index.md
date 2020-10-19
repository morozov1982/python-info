# Встроенные функции

`abs()` - возвращает абсолютное значение числа

``` Python 3
abs(-10)  # вернёт 10
abs(-3.14)  # вернёт 3.14
```

`all()` - вернёт True, если все элементы итерируемого объекта True
(или если объект пустой) [all_any.py](all_any.py)

`any()` - вернёт True, если хотя бы один элемент
итерируемого объекта True (если объект пустой - False) [all_any.py](all_any.py)

ascii()

bin()

bool()

breakpoint()

bytearray()

bytes()

callable()

chr()

classmethod()

compile()

complex()

delattr()

dict()

dir()

divmod()

enumerate()

eval()

exec()

`filter()` - возвращает итератор, из элементов списка отфильтрованных в соответствии с функцией. По простому - вернуть только нужное, убрать ненужное [filter.py](filter.py)

``` Python3
# filter(func, iterable)

def has_o(string):
    return 'o' in string.lower()

words = ['One', 'two', 'three', '23Fkjsf']
filtered_list = list(filter(has_o, words))  # ['One', 'two']
```

``` Python3
# с использованием lambda
filtered_list = list(filter(lambda string: 'o' in string.lower(), words))  # ['One', 'two']

# с использованием генератора
comp_list = [string for string in words if has_o(string)]  # ['One', 'two']
```

float()

format()

frozenset()

getattr()

globals()

hasattr()

hash()

help()

hex()

id()

input()

int()

isinstance()

issubclass()

iter()

len()

list()

locals()

`map()` - возвращает итератор, который применяет функцию к каждому элементу итерации, (yielding) результат. По простому - применить функцию к каждому элементу в итераторе [map.py](map.py)

``` Python3
# map(func, *iterable)

def upper(string):
    return string.upper()

lower_list = ['one', 'two', 'three']
upper_list = list(map(upper, lower_list))  # ['ONE', 'TWO', 'THREE']
```

``` Python3
# с использованием lambda
upper_list = list(map(lambda string: string.upper(), lower_list))  # ['ONE', 'TWO', 'THREE']

# с использованием генератора
comp_upper_list = [string.upper() for string in lower_list]  # ['ONE', 'TWO', 'THREE']
```

max()

memoryview()

min()

next()

object()

oct()

open()

ord()

pow()

print()

property()

range()

repr()

reversed()

round()

set()

setattr()

slice()

sorted()

staticmethod()

str()

sum()

super()

tuple()

type()

vars()

zip()

\_\_import__()