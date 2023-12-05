import re


with open("input.txt") as f:
    input_seeds, *input_maps = f.read().strip().split("\n\n")

seeds_pattern = r"^seeds: ((?: ?\d+)+)$"
map_pattern = r"^(\d+) (\d+) (\d+)$"

def map_number(number: int, map: list[tuple[range, range]]) -> int:
    for dest_map, src_map in map:
        if number in src_map:
            index = src_map.index(number)
            return dest_map[index]

    return number     

maps = []

for map in input_maps:
    current_map = []
    lines = map.split("\n")[1:]

    for line in lines:
        #print(line, repr(line))
        map_match = re.match(map_pattern, line)
        dest_start = int(map_match.group(1))
        src_start = int(map_match.group(2))
        length = int(map_match.group(3))

        current_map.append((range(dest_start, dest_start + length), range(src_start, src_start + length)))
    
    maps.append(current_map)

seeds = [int(seed) for seed in re.match(seeds_pattern, input_seeds).group(1).split(" ")]

mapped_seeds = seeds.copy()

for map in maps:
    for i, seed in enumerate(mapped_seeds):
        mapped_seeds[i] = map_number(seed, map)

print(min(mapped_seeds))
