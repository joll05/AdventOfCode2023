import re


with open("input.txt") as f:
    input_directions, input_connections = f.read().strip().split("\n\n")
    input_connections = input_connections.split("\n")

directions = tuple(map(lambda s: 0 if s == "L" else 1, input_directions))

connection_pattern = r"^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)$"

connections = {}

for line in input_connections:
    connection_match = re.match(connection_pattern, line)
    connections[connection_match.group(1)] = (connection_match.group(2), connection_match.group(3))

current_node = "AAA"
steps = 0

while current_node != "ZZZ":
    current_direction = directions[steps % len(directions)]
    current_node = connections[current_node][current_direction]
    steps += 1

print(steps)
    