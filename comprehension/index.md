# Генераторы (comprehension)

## Общая формула

`(values) = [ (expression) for (value) in (collection) ]`

Пример: [файл](list_comprehension.py)
``` Python 3
jack = {
    'name': 'Jack',
    'car': 'BMW'
}

john = {
    'name': 'John',
    'car': 'Audi'
}

users = [jack, john]  # список словарей

# вариант с генератором
cars = [person.get('car', 'нет машины') for person in users]  # ['BMW', 'Audi']

# авриант с циклом for
cars = []
for person in users:
    cars.append(person.get('car', 'нет машины'))
```

## Фильтрация (if)

`(values) = [ (expression) for (value) in (collection) if (condition) ]`

Пример: [файл](list_comprehension.py)
``` Python 3
# вариант с генератором
new_names = [n for n in names if n.startswith('J')]  # ['Jack', 'John']

# авриант с циклом for
new_names = []
for n in names:
    if n.startswith('J'):
        new_names.append(n)
```