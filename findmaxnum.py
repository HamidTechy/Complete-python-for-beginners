number = [34, 75, 72, 63]
print(max(number))

import utils
number = [34, 55, 72, 63]

max = utils.find_max(number)
print(max)


number = [34, 85, 42, 63]
max = number[0]
for item in number:
    if item > max:
        max = item
print(max)