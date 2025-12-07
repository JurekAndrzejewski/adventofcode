INPUT = 'input.txt'

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

ranges, numbers = read_file()

counter = 0
for number in numbers:
    for range in ranges:
        if number >= range[0] and number <= range[1]:
            print(number)
            counter += 1
            break
print('|',counter)