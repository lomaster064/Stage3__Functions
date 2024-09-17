data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum = 0


def calculate_structure_sum(*args):
    global sum

    for i in args:
        if isinstance(i, (int, float)):
            sum += i
        if isinstance(i, str):
            sum += len(i)

        if isinstance(i, (list, tuple, set)):
            for j in i:
                if isinstance(j, (int, float)):
                    sum += j
                if isinstance(j, str):
                    sum += len(j)

                if isinstance(j, (list, tuple, set)):
                    calculate_structure_sum(*j)

                if isinstance(j, dict):
                    calculate_structure_sum(j)

        if isinstance(i, dict):
            for k, v in i.items():
                sum += len(k)

                if isinstance(v, (int, float)):
                    sum += v
                if isinstance(v, str):
                    sum += len(v)

    return sum


sum_chars = calculate_structure_sum(*data_structure)
print(sum_chars)  # Output: 132