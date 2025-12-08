import operator

INPUT = 'input.txt'
ops = {"+": operator.add, "*": operator.mul}

li = []
with open(INPUT, 'r', encoding='utf-8') as f:
    line = f.readline()
    for c, element in enumerate(line):
        li.append([element])
    for i, line in enumerate(f.readlines()):
        for c, element in enumerate(line):
            li[c].append(element)

print(li)
new_numbers = []
for number in li:
    if len(set(number)) == 1:
        pass
    else:
        new_numbers.append(number)

result = 0
results = []
for number in new_numbers:
    number = "".join(number)
    if number[-1] in ops.keys():
        print(results.append(result))
        print("_____________")
        op = number[-1]
        correct_number = number[:-1]
        result = 1 if op == "*" else 0
        #print(f"{result}{op}{int(correct_number)}")
        result = ops[op](result, int(correct_number))
    else:
        #print(f"{result}{op}{int(number)}")
        result = ops[op](result, int(number))
results.append(result)

print(results)
print(sum(results))