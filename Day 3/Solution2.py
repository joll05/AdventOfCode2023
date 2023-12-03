import re


with open("input.txt") as f:
    input_text = f.read().strip();

width = input_text.find("\n") + 1 # this will include the newline characters, but since they are not special characters it shouldn't matter
height = input_text.count("\n") + 1

def pos_to_xy(pos):
    return (pos % width, pos // width)

def xy_to_pos(x, y):
    return y * width + x

number_pattern = r"(\d+)"
symbol_pattern = r"([^\.\n\d])"
gear_pattern = r"\*"

numbers_iter = re.finditer(number_pattern, input_text)
numbers = {(int(num.group(0)), range(num.start(), num.end())) for num in numbers_iter}

gears_iter = re.finditer(gear_pattern, input_text)

result = 0

for gear in gears_iter:
    gear_pos = gear.start()

    gear_x, gear_y = pos_to_xy(gear_pos)

    rect_min_x = max(gear_x - 1, 0)
    rect_max_x = min(gear_x + 1, width - 1)
    rect_min_y = max(gear_y - 1, 0)
    rect_max_y = min(gear_y + 1, height - 1)

    surrounding_numbers = []

    for number, span in numbers:
        for x in range(rect_min_x, rect_max_x + 1):
            do_exit = False
            for y in range(rect_min_y, rect_max_y + 1):
                pos = xy_to_pos(x, y)
                if pos in span:
                    surrounding_numbers.append(number)
                    do_exit = True
                    break
            
            if do_exit:
                break
    
    if len(surrounding_numbers) == 2:
        result += surrounding_numbers[0] * surrounding_numbers[1]

print(result)
