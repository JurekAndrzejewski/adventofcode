"""INPUT = 'test.txt'

def read_file():
    with open(INPUT, 'r', encoding = 'utf-8') as f:
        ranges = []
        numbers = []
        ranges_flag = True
        for line in f.readlines():
            if line.strip() == "":
                ranges_flag = False
                continue
            if ranges_flag:
                ranges.append([int(line.strip().split('-')[0]), int(line.strip().split('-')[1])])
            else:
                numbers.append(int(line.strip()))
    return ranges, numbers
    
def get_fresh_ingredients(ranges):
    fresh_ingredients = []
    new_ranges = []
    for prop_range in ranges:
        if not new_ranges:
            new_ranges.append(prop_range)
            continue
        for exist_range in new_ranges:
            print('prop_range | exist_range')
            print(f'{prop_range} | {exist_range}')
            if ((prop_range[0] > exist_range[0]) and (prop_range[1] < exist_range[1])):
                break
            elif ((prop_range[0] < exist_range[0]) and ((prop_range[1] < exist_range[1]) and (prop_range[1] > exist_range[0]))):
                exist_range[0] = prop_range[0]
                break
            elif (((prop_range[0] > exist_range[0]) and (prop_range[0] < exist_range[1])) and (prop_range[1] > exist_range[1])):
                exist_range[1] = prop_range[1]
                break
            else:
                new_ranges.append(prop_range)
    return new_ranges

ranges, numbers = read_file()
fresh_ingredients = get_fresh_ingredients(ranges)

print(fresh_ingredients)"""

exist_range = [5 ,10]
prop_range = [4, 8]
if ((prop_range[0] > exist_range[0]) and (prop_range[1] < exist_range[1])):
    print('a')
elif ((prop_range[0] < exist_range[0]) and ((prop_range[1] < exist_range[1]) and (prop_range[1] > exist_range[0]))):
    exist_range[0] = prop_range[0]
    print('b')
elif (((prop_range[0] > exist_range[0]) and (prop_range[0] < exist_range[1])) and (prop_range[1] > exist_range[1])):
    exist_range[1] = prop_range[1]
    print('c')
elif (prop_range[0] < exist_range[0]) and (prop_range[1] > exist_range[1]):
    print('d')
elif prop_range == exist_range:
    print('e')