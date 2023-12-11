with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

galaxies = []

col_empty = [True] * len(input_lines[0])
row_empty = [True] * len(input_lines)

for y, line in enumerate(input_lines):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append((x, y))
            col_empty[x] = False
            row_empty[y] = False

empty_cols = [i for i, empty in enumerate(col_empty) if empty]
empty_rows = [i for i, empty in enumerate(row_empty) if empty]

total = 0

for i, (g1_x, g1_y) in enumerate(galaxies):
    for (g2_x, g2_y) in galaxies[i + 1:]:
        x_expansion = len([c for c in empty_cols if min(g1_x, g2_x) < c < max(g1_x, g2_x)])
        y_expansion = len([r for r in empty_rows if min(g1_y, g2_y) < r < max(g1_y, g2_y)])

        dist = abs(g1_x - g2_x) + abs(g1_y - g2_y) + (x_expansion + y_expansion) * (1000000 - 1)
        total += dist

print(total)