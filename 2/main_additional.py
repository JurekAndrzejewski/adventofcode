from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

INPUT = 'input.txt'

def get_numbers():
    with open(INPUT, 'r', encoding='utf-8') as f:
        temp_list = f.read().split(',')
        return_list = []
        for x in temp_list:
            values = x.split('-')
            return_list.append([int(values[0]), int(values[1])])
        return return_list

def checker(number):
    appearances = []
    number = str(number)
    for x in range(1,len(number)):
        window = number[0:int(x)]
        #print(f"window | {window}")
        length = len(window)
        start = int(x)
        end = int(x)+length
        z_vals = []
        z_vals.append(window)
        while end <= len(number):
            z = number[start:end]
            z_vals.append(z)

            end += length
            start += length
        #print(z_vals)
        if z_vals != [window]:
            if all_equal(z_vals) and "".join(z_vals)==number:
                print(z_vals, end, len(number))
                return True
        appearances.append(x)


numbers = get_numbers()
result = 0
for values in numbers:
    for x in range(values[0], values[1]+1):
        if checker(x):
            result += x
            print(x)
print(result)