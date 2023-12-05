# This works, but took 13 mins 22 seconds to run on my machine :P

import re
import time

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

def map_number_reverse(number: int, map: list[tuple[range, range]]) -> int:
    for src_map, dest_map in map:
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

seed_data = [int(seed) for seed in re.match(seeds_pattern, input_seeds).group(1).split(" ")]

seed_ranges = [range(seed_data[i], seed_data[i] + seed_data[i+1]) for i in range(0, len(seed_data), 2)]

done = False
i = 0
last_print = 0
start_time = time.time()
while not done:
    if time.time() - last_print > 5:
        print(i)
        last_print = time.time()

    mapped_number = i
    for map in maps[::-1]:
        mapped_number = map_number_reverse(mapped_number, map)
    
    for seed_range in seed_ranges:
        if mapped_number in seed_range:
            print(f"Answer: {i}\nTime: {time.time() - start_time}")
            done = True
            break
    
    i += 1