def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(23, False)
print_params()
print_params(a = [1, 2, 3])

values_list = [2.0, True, 'String']
values_dict = {'a': 3, 'b': False, 'c': {1, 2, 3}}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['str', [[1, 2, 3], [4, 5, 6]]]
print_params(*values_list_2)
print_params(*values_list_2, 42)