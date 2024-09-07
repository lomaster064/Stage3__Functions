calls = 0

def count_calls():
    global calls

    calls += 1

def string_info(string):
    cnt = len(string)
    upr_str = string.upper()
    lwr_str = string.lower()

    res = tuple([cnt, upr_str, lwr_str])
    count_calls()
    return res

def is_contains(string, list_to_search):
    res = False
    for i in list_to_search:
        if i.upper() == string.upper():
            res = True
        else:
            res = False

    count_calls()
    return res


print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)