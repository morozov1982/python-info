list_0 = []
list_1 = [True, True, True]
list_2 = [True, True, False]
list_3 = [False, False, False]
list_4 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
list_5 = [-5, -4, -3, -2, -1]
list_6 = [0, 1, 2, 3, 4, 5]
list_7 = [1, 2, 3, 4, 5]
list_8 = ['a', 'b', 'c']
list_9 = [True, True, True, [False, False, False]]
list_a = [False, False, False, [True, True, True]]

print('all()\n')

print(list_0, '-->', all(list_0))  # [] --> True
print(list_1, '-->', all(list_1))  # [True, True, True] --> True
print(list_2, '-->', all(list_2))  # [True, True, False] --> False
print(list_3, '-->', all(list_3))  # [False, False, False] --> False
print(list_4, '-->', all(list_4))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] --> False
print(list_5, '-->', all(list_5))  # [-5, -4, -3, -2, -1] --> True
print(list_6, '-->', all(list_6))  # [0, 1, 2, 3, 4, 5] --> False
print(list_7, '-->', all(list_7))  # [1, 2, 3, 4, 5] --> True
print(list_8, '-->', all(list_8))  # ['a', 'b', 'c'] --> True
print(list_9, '-->', all(list_9))  # [True, True, True, [False, False, False]] --> True
print(list_a, '-->', all(list_a))  # [False, False, False, [True, True, True]] --> False

print('\n\nany()\n')

print(list_0, '-->', any(list_0))  # [] --> False
print(list_1, '-->', any(list_1))  # [True, True, True] --> True
print(list_2, '-->', any(list_2))  # [True, True, False] --> True
print(list_3, '-->', any(list_3))  # [False, False, False] --> False
print(list_4, '-->', any(list_4))  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] --> True
print(list_5, '-->', any(list_5))  # [-5, -4, -3, -2, -1] --> True
print(list_6, '-->', any(list_6))  # [0, 1, 2, 3, 4, 5] --> True
print(list_7, '-->', any(list_7))  # [1, 2, 3, 4, 5] --> True
print(list_8, '-->', any(list_8))  # ['a', 'b', 'c'] --> True
print(list_9, '-->', any(list_9))  # [True, True, True, [False, False, False]] --> True
print(list_a, '-->', any(list_a))  # [False, False, False, [True, True, True]] --> True
