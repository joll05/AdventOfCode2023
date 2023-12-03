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

numbers = re.finditer(number_pattern, input_text)

result = 0

for number in numbers:
    span_min, span_max = number.span()

    span_min_x, span_y = pos_to_xy(span_min)
    span_max_x, _ = pos_to_xy(span_max)

    rect_min_x = max(span_min_x - 1, 0)
    rect_max_x = min(span_max_x, width - 1)
    rect_min_y = max(span_y - 1, 0)
    rect_max_y = min(span_y + 1, height - 1)

    has_symbol = False

    for x in range(rect_min_x, rect_max_x + 1):
        for y in range(rect_min_y, rect_max_y + 1):
            pos = xy_to_pos(x, y)
            if re.match(symbol_pattern, input_text[pos]):
                has_symbol = True
    
    if has_symbol:
        result += int(number.group(0))

print(result)
