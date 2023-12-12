from functools import lru_cache


with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

inputs = []

for line in input_lines:
    springs, groups = line.split(" ")
    inputs.append((
        tuple(map(lambda s: -1 if s == "." else 1 if s == "#" else 0, springs)),
        tuple(map(int, groups.split(",")))
    ))

@lru_cache(maxsize=None)
def possible_arrangements(springs: tuple[int], groups: tuple[int]):
    if len(groups) == 0:
        if 1 in springs: return 0
        else: return 1

    first_broken = springs.index(1) + 1 if 1 in springs else len(springs)
    
    total = 0

    for i in range(min(len(springs) - groups[0] + 1, first_broken)):
        can_fit = all(spring >= 0 for spring in springs[i:i+groups[0]])
        can_fit = can_fit and (i - 1 < 0 or springs[i - 1] <= 0) and (i + groups[0] >= len(springs) or springs[i + groups[0]] <= 0)
        
        if not can_fit: continue

        total += possible_arrangements(springs[i+groups[0]+1:], groups[1:])
    
    return total

result = 0

for i, (springs, groups) in enumerate(inputs):
    result += possible_arrangements(((springs + (0,)) * 5)[:-1], groups * 5)
    print(i)

print(result)