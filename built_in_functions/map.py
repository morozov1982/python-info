# map(func, *iterable)

# Как работает map()
# def map(func, iterable):
#     for i in iterable:
#         yield func(i)

def upper(string):
    return string.upper()


lower_list = ['one', 'two', 'three']
upper_list = list(map(upper, lower_list))
print('upper_list:', upper_list)

lambda_upper_list = list(map(lambda string: string.upper(), lower_list))
print('lambda_upper_list:', lambda_upper_list)

comp_upper_list = [string.upper() for string in lower_list]
print('comp_upper_list:', comp_upper_list)
