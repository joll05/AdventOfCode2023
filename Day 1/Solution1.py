with open("input.txt") as f:
    input_lines = f.read().strip().split("\n");

result = 0

for line in input_lines:
    number = ""

    for char in line:
        if "0" <= char <= "9":
            number += char
            break
    
    for char in line[::-1]:
        if "0" <= char <= "9":
            number += char
            break
    
    result += int(number)

print(result)