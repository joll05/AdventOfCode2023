with open("input.txt") as f:
    input_lines = f.read().strip().split("\n");

numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

result = 0

def is_number(line: str, index: int):
    if "0" <= line[index] <= "9":
        return int(line[index])
    
    for i, number in enumerate(numbers):
        if line[index:].startswith(number):
            return i
    
    return None

for line in input_lines:

    print("\n" + line)
    number1 = None
    for i in range(len(line)):
        number_result = is_number(line, i)
        if number_result != None:
            number1 = number_result
            print(number1, line[i:i+5])
            break
    
    number2 = None
    for i in range(len(line) - 1, -1, -1):
        number_result = is_number(line, i)
        if number_result != None:
            number2 = number_result
            print(number2, line[i:i+5])
            break
    
    result += number1 * 10 + number2

print(result)