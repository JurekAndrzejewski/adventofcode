INPUT = 'input.txt'
result = []
with open(INPUT, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        max_joules = 0
        for c, number in enumerate(line[:-1]):
            for next_number in line[1+c:]:
                joules = int(number+next_number)
                if joules > max_joules:
                    max_joules = joules
        result.append(max_joules)
print(sum(result))