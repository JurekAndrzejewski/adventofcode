INPUT = 'input.txt'

class DialNumber(int):
    def __init__(self, val=0):
        self._val = int(val)
    def add(self, other, bigCounter):
        for _ in range(other):
            self._val += 1
            if self._val == 100:
                self._val = 0
                bigCounter += 1
        return DialNumber(self._val), bigCounter
    def subtract(self, val, bigCounter):
        for _ in range(val):
            self._val -= 1
            if self._val == 0:
                bigCounter += 1
            if self._val == -1:
                self._val = 99
        return DialNumber(self._val), bigCounter

curr_val = DialNumber(50)
counter = 0
bigCounter = 0

with open(INPUT, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        rotation = line[0]
        number = int(line[1:])
        if rotation == 'L':
            curr_val, bigCounter = curr_val.subtract(number, bigCounter)
        else:
            curr_val, bigCounter = curr_val.add(number, bigCounter)
        if curr_val == 0:
            counter += 1
    print(counter, bigCounter)