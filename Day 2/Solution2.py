import re

with open("input.txt") as f:
    input_lines = f.read().strip().split("\n");

game_pattern = r"^Game (\d+): (.*)$"

cubes_pattern = r"^(\d+) (red|green|blue)$"

result = 0

for line in input_lines:
    game_match = re.match(game_pattern, line)
    game = game_match.group(2)

    rounds = game.split("; ")

    max_cubes = {
        "red": 0,
        "green": 0,
        "blue" : 0
    }

    for round in rounds:
        cubes = round.split(", ")

        for cube in cubes:
            cube_match = re.match(cubes_pattern, cube)
            count = int(cube_match.group(1))
            color = cube_match.group(2)

            if(count > max_cubes[color]):
                max_cubes[color] = count
        
    power = max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

    result += power

print(result)