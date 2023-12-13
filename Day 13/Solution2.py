with open("input.txt") as f:
    input_grids = f.read().strip().split("\n\n")

grids = []

for grid in input_grids:
    grid_lines = grid.split("\n")
    grids.append([[char == "#" for char in line] for line in grid_lines])

total = 0

for grid in grids:
    for y in range(len(grid) - 1):
        differences = 0

        for check in range(min(y + 1, len(grid) - y - 1)):
            differences += [el1 ^ el2 for el1, el2 in zip(grid[y - check], grid[y + check + 1])].count(True)

        if differences == 1:
            total += (y + 1) * 100
            break
    
    for x in range(len(grid[0]) - 1):
        differences = 0

        for check in range(min(x + 1, len(grid[0]) - x - 1)):
            differences += [row[x - check] ^ row[x + check + 1] for row in grid].count(True)

        if differences == 1:
            total += x + 1
            break

print(total)
                
        
