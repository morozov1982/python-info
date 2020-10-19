# filter(func, iterable)

def has_o(string):
    return 'o' in string.lower()


words = ['One', 'two', 'three', '23Fkjsf']
filtered_list = list(filter(has_o, words))
print('filtered_list:', filtered_list)

lambda_filtered_list = list(filter(lambda string: 'o' in string.lower(), words))
print('lambda_filtered_list:', lambda_filtered_list)

comp_list = [string for string in words if has_o(string)]
print('comp_list:', comp_list)
