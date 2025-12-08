import operator

INPUT = 'input.txt'
ops = {"+": operator.add, "*": operator.mul}

li = []
with open(INPUT, 'r', encoding='utf-8') as f:
    line = f.readline()
    for c, element in enumerate(line.split()):
        li.append([element])
    for i, line in enumerate(f.readlines()):
        for c, element in enumerate(line.split()):
            li[c].append(element)


li = [x[::-1] for x in li]

results = []
for x in li:
    result = ops[x[0]](int(x[1]),int(x[2]))
    for z in x[3:]:
        result = ops[x[0]](int(z), result)
    results.append(result)
print(results)
print(sum(results))