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
    number = str(number)
    length = int(len(number)/2)
    half1 = number[:length]
    half2 = number[length:]
    return half1==half2

numbers = get_numbers()

result = 0
for values in numbers:
    for x in range(values[0], values[1]+1):
        if checker(x):
            result += x
print(result)