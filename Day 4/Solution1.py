import re


with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

card_pattern = r"Card +(\d+): ((?: ?[ \d]\d)+) \| ((?: ?[ \d]\d)+)"

points = 0

for line in input_lines:
    # print(line)
    card_match = re.match(card_pattern, line)

    winners = {int(number) for number in card_match.group(2).split(" ") if number != ""}
    card_numbers = {int(number) for number in card_match.group(3).split(" ") if number != ""}

    winning_numbers = winners.intersection(card_numbers)

    if(len(winning_numbers) > 0):
        points += 2 ** (len(winning_numbers) - 1)

print(points)