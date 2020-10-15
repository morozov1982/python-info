jack = {
    'name': 'Jack',
    'car': 'BMW'
}

john = {
    'name': 'John',
    'car': 'Audi'
}

users = [jack, john]  # список словарей

# авриант с циклом for
cars = []
for person in users:
    cars.append(person.get('car', 'нет машины'))  # person.get('car', '') лучше чем антипаттерн person['car']

# вариант с генератором
cars = [person.get('car', 'нет машины') for person in users]

print('Cars:', cars)


# фильтрация (if)
names = ['Jack', 'John', 'Oleg', 'Ula']

# авриант с циклом for
new_names = []
for n in names:
    if n.startswith('J'):
        new_names.append(n)

# вариант с генератором
new_names = [n for n in names if n.startswith('J')]

print('New_names:', new_names)
