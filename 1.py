INPUT = 'input.txt'

class DialNumber(int):
    def __init__(self, val=0):
        self._val = int(val)
    def __add__(self, other):
        for _ in range(other):
            self._val += 1
            if self._val == 100:
                self._val = 0
        return DialNumber(self._val)
    def __sub__(self, val):
        for _ in range(val):
            self._val -= 1
            if self._val == -1:
                self._val = 99
        return DialNumber(self._val)

curr_val = DialNumber(50)
counter = 0

with open(INPUT, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        rotation = line[0]
        number = int(line[1:])
        if rotation == 'L':
            curr_val = curr_val - number
        else:
            curr_val = curr_val + number
        if curr_val == 0:
            counter += 1
    print(counter)