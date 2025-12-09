from copy import deepcopy
import collections
INPUT = 'input.txt'


#new_lines = []
with open(INPUT, 'r', encoding = 'utf-8') as f:
    first_line = f.readline()
    beam_indices = {first_line.index('S'): 1}
    for c, line in enumerate(f.readlines()):
        new_beam_indices = deepcopy(beam_indices)
        for beam_index in beam_indices.keys():
            if line[beam_index] == '^':
                if beam_index-1 in new_beam_indices.keys():
                    new_beam_indices[beam_index-1] += 1*new_beam_indices[beam_index]
                else:
                    new_beam_indices[beam_index-1] = new_beam_indices[beam_index]
                if beam_index+1 in new_beam_indices.keys():
                    new_beam_indices[beam_index+1] += 1*new_beam_indices[beam_index]
                else:
                    new_beam_indices[beam_index+1] = new_beam_indices[beam_index]
                del new_beam_indices[beam_index]
        beam_indices = new_beam_indices
        print(line.strip(), dict(collections.OrderedDict(sorted(beam_indices.items()))))

od = collections.OrderedDict(sorted(beam_indices.items()))

for x in od:
    print(f"{x}:{od[x]}")

print(sum(list(od.values())))