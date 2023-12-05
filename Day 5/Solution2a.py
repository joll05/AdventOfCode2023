# I think this will theoretically work with unlimited time and memory, but it runs into a MemoryError

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

def map_range(range_to_map: range, map: list[tuple[range, range]]) -> list[range]:
    ranges = [range_to_map]

    remapped = []

    for r in ranges:
        new_ranges = []

        for dest_map, src_map in map:
            offset = dest_map.start - src_map.start
            if src_map.start >= r.stop or src_map.stop <= r.start:
                # map doesn't contain range
                new_ranges.append(r)
            elif src_map.start <= r.start and src_map.stop < r.stop:
                # map contains left side of range
                remapped.append(range(r.start + offset, src_map.stop + offset))
                new_ranges.append(range(src_map.stop, r.stop))
            elif src_map.start > r.start and src_map.stop >= r.stop:
                # map contains right side of range
                remapped.append(range(src_map.start + offset, r.stop + offset))
                new_ranges.append(range(r.start, src_map.start))
            elif src_map.start > r.start and src_map.stop < r.stop:
                # map is contained within range
                remapped.append(dest_map)
                new_ranges.append(range(r.start, src_map.start))
                new_ranges.append(range(src_map.stop, r.stop))
            else:
                # range is completely contained within map
                remapped.append(range(r.start + offset, r.stop + offset))

        ranges = new_ranges
    
    return remapped + ranges

def map_ranges(ranges: list[range], map: list[tuple[range, range]]) -> list[range]:
    result = []

    for original_range in ranges:
        result += map_range(original_range, map)
    
    return result

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

mapped_ranges = seed_ranges.copy()

for i, map in enumerate(maps):
    print(i, len(mapped_ranges))
    mapped_ranges = map_ranges(mapped_ranges, map)

print(len(mapped_ranges))

print(min(mapped_ranges, key=lambda x: x.start))