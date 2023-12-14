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
    # Called it

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

rock_history = [movable_rocks]
loop_point = 0

while True:
    next_rocks = move_rocks((0, -1), rock_history[-1], stationary_rocks, w, h)
    next_rocks = move_rocks((-1, 0), next_rocks, stationary_rocks, w, h)
    next_rocks = move_rocks((0, 1), next_rocks, stationary_rocks, w, h)
    next_rocks = move_rocks((1, 0), next_rocks, stationary_rocks, w, h)

    if next_rocks in rock_history:
        loop_point = rock_history.index(next_rocks)
        break
    
    rock_history.append(next_rocks)

total = 0

for x, y in rock_history[loop_point + (1_000_000_000 - loop_point) % (len(rock_history) - loop_point)]:
    total += h - y

print(total) 