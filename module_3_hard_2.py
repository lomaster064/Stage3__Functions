data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

string_ = str(data_structure)
list_ = ['[', ']', '{', '}', '(', ')', '"', "'", ':', ' ']
sum = 0


def replace_string(st, *args):
    global sum
    new_string = st

    for i in args:
        if i == ':':
            new_string = new_string.replace(i, ',')
        else:
            new_string = new_string.replace(i, '')

    new_list = list(new_string.split(","))
    for j in new_list:
        if j == '':
            continue

        try:
            sum += int(j)
        except:
            sum += len(j)

    return sum

sum_chars = replace_string(string_, *list_)
print(sum_chars)
