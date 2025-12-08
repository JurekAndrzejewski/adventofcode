INPUT = 'input.txt'

def read_file():
    with open(INPUT, 'r', encoding = 'utf-8') as f:
        ranges = []
        for line in f.readlines():
            if line.strip() == "":
                return ranges
            ranges.append([int(line.strip().split('-')[0]), int(line.strip().split('-')[1])])
    return ranges

def overlap_checker(ranges):
    print("overlap_checker")
    new_ranges = [ranges[0]]
    for r in ranges[1:]:
        prev = new_ranges[-1]
        print(prev, r)
        if prev[1] >= r[0]:
            print('overlap')
            prev[1] = max(prev[1], r[1])
        else:
            print('no overlap')
            new_ranges.append(r)
        print(new_ranges)
    return new_ranges

ranges = read_file()
ranges = sorted(ranges, key=lambda x: x[0])

length = len(ranges)
new_length = 0
while True:
    length = len(ranges)
    ranges = overlap_checker(ranges)
    new_length = len(ranges)
    if length == new_length:
        break

c = 0
for new_range in ranges:
    c += new_range[1]-new_range[0]+1
print(c)