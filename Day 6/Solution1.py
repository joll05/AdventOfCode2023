from math import sqrt, floor, ceil
import re

with open("input.txt") as f:
    input_data = f.read().strip()

"""
Variable definitions:
t = total race time
c = charge time
r = travelling time
d = distance travelled

The total time to race is the sum of charge and travelling time
t = c + r <=> r = t - c

The distance travelled is the travelling time times the charge time
d = cr
d = c(t - c)
d = ct - c^2
ct - c^2 - d = 0

Multiply both sides by -1 and rearrange

c^2 - ct + d = 0

we can solve for c using the quadratic formula

c = t/2 +- sqrt((t/2)^2 - d)
c = t/2 +- sqrt(t^2/4 - d)

c_min = t/2 - sqrt(t^2/4 - d)
c_max = t/2 - sqrt(t^2/4 - d)

If you plug in the total race time and the record distance, you get a minimum and maximimum charge time
To make them into integer results, ceil min and floor max
"""

data_pattern = r"^Time: +([ \d]+)\nDistance: +([ \d]+)$"
split_pattern = r" +"

data_match = re.match(data_pattern, input_data)
times = map(int, re.split(split_pattern, data_match.group(1)))
distances = map(int, re.split(split_pattern, data_match.group(2)))
races = zip(times, distances)

result = 1

for time, distance in races:
    root = sqrt(time ** 2 / 4 - distance)
    min_charge = ceil(time / 2 - root)
    max_charge = floor(time / 2 + root)
    result *= (max_charge - min_charge + 1)

print(result)