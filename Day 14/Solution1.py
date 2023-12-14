from typing import NamedTuple

with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

w = len(input_lines[0])
h = len(input_lines)

movable_rocks = set()
stationary_rocks = set()

for y, line in enumerate(input_lines):
    for x, char in enumerate(line):
        if char == "O":
            movable_rocks.add((x, y))
        elif char == "#":
            stationary_rocks.add((x, y))

def move_rocks(direction, movable, stationary, w, h):
    # I'm don't really need direction right now, but I assume I will need it in part 2

    movable_sorted = sorted(movable, key=lambda r: r[0] * direction[0] + r[1] * direction[1], reverse=True)

    new_movable = set()

    for rock in movable_sorted:
        pos = rock

        while True:
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])

            if not (0 <= next_pos[0] < w) or not (0 <= next_pos[1] < h) or next_pos in new_movable or next_pos in stationary:
                new_movable.add(pos)
                break

            pos = next_pos

    return new_movable

movable_rocks = move_rocks((0, -1), movable_rocks, stationary_rocks, w, h)

total = 0

for x, y in movable_rocks:
    total += h - y

print(total) 