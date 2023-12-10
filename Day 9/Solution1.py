with open("input.txt") as f:
    input_lines = f.read().strip().split("\n")

inputs = tuple(tuple(map(int, line.split(" "))) for line in input_lines)

result = 0

for values in inputs:
    diffs = [values]

    while any(diffs[-1]): # While all is not 0 (false)
        diffs.append(tuple(diffs[-1][i + 1] - diffs[-1][i] for i in range(len(diffs[-1]) - 1)))
    
    addition = 0

    for diff in diffs[::-1][1:]:
        addition = diff[-1] + addition
    
    result += addition

print(result)