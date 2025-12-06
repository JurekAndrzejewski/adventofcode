INPUT = 'test.txt'

class DialNumber(int, int):
    def __init__(self, val=0, bigCounter = 0):
        self._val = int(val)
        self.bigCounter = bigCounter
    def __add__(self, other):
        print(self.bigCounter)
        for _ in range(other):
            self._val += 1
            if self._val == 100:
                self._val = 0
                self.bigCounter += 1
                print(self.bigCounter)
        return DialNumber(self._val, self.bigCounter)
    def __sub__(self, other):
        for _ in range(other):
            self._val -= 1
            if self._val == 0:
                self.bigCounter += 1
            if self._val == -1:
                self._val = 99
        return DialNumber(self._val, self.bigCounter)
    def getBigCounter(self):
        return self.bigCounter

curr_val = DialNumber(val=50, bigCounter=50)
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
    print(curr_val.getBigCounter())