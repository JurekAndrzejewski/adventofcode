INPUT = 'input.txt'
result = []

def get_max_val(line, max_vals_length):
    #print("line |" + f"{line}".rjust(15))
    line2 = [int(x) for x in line]
    max_val = max(line2)
    index = line2.index(max_val)
    while (len(line2) - index) < 12-max_vals_length:
        max_val = max(line2[:index])
        index = line2.index(max_val)
    return max_val, line[index+1:]

with open(INPUT, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        max_vals = []
        for x in range(12):
            max_val, line = get_max_val(line, len(max_vals))
            max_vals.append(str(max_val))
        print(int(''.join(max_vals)))
        result.append(int(''.join(max_vals)))
print(sum(result))