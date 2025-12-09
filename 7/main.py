INPUT = 'test.txt'

new_lines = []
result = 0
with open(INPUT, 'r', encoding = 'utf-8') as f:
    first_line = f.readline()
    beam_indices = [first_line.index('S')]
    new_lines.append(first_line.strip())
    for c, line in enumerate(f.readlines()):
        new_beam_indices = []
        for beam_index in beam_indices:
            if line[beam_index] == '^':
                result += 1
                new_beam_indices.append(beam_index-1)
                new_beam_indices.append(beam_index+1)
            else:
                new_beam_indices.append(beam_index)
        if new_beam_indices:
            beam_indices = set(new_beam_indices)
        new_line = list(line.strip())
        for i in beam_indices:
            new_line[i] = '|'
        new_lines.append(''.join(new_line))


for x in new_lines:
    print(x)

print(result)