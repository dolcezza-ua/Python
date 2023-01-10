# 1. Create a list with different data types and display all of its elements in three different ways.

mix = [0, "cat", -2, True, 10.2, None, 25, "1231", False]

print(mix)                     # [0, 'cat', -2, True, 10.2, None, 25, '1231', False]

for i in range(len(mix)):       
print(mix[i])                  # 0 cat -2 True 10.2 None 25 1231 False

for _ in mix:
    print(_)                   # 0 cat -2 True 10.2 None 25 1231 False

# 2. Unlike a character in a string, an element in a list can be: 
# - replaced by its index, 
# - add a new element to the end of the list or to a specific place in the list, 
# - remove the last element from the list, or any other.

# 0, 2 and the last element in the "mix" list replace by elements 45, 22 and 15, respectively:

mix = [0, "cat", -2, True, 10.2, None, 25, "1231", False]
mix [0] = 45
mix [2] = 22
mix [-1] = 15

print(mix)               # [45, 'cat', 22, True, 10.2, None, 25, '1231', 15]

# add number 1000 to the end of the list and number 200 to the second place in the list:

mix.append(1000)
mix.insert(2, 200)

print(mix)               # [45, 'cat', 200, 22, True, 10.2, None, 25, '1231', 15, 1000]

# add a new list [1100, 1200, 1300] to the end of the "mix" list:

mix.extend([1100, 1200, 1300])

print(mix)               # [45, 'cat', 200, 22, True, 10.2, None, 25, '1231', 15, 1000, 1100, 1200, 1300]

# remove the last element from the list and the first:

a = mix.pop()
b = mix.pop(1)

print(a, b)              # 1300 cat
print(mix)               # [45, 200, 22, True, 10.2, None, 25, '1231', 15, 1000, 1100, 1200]

# 3. Convert the string "I am Olha" to a list:

arr = list("I am Olha")
print(arr)               # ['I', ' ', 'a', 'm', ' ', 'O', 'l', 'h', 'a']

# Create a list of 30 elements where each element is 0:

arr2 = [0] * 30
print(arr2)              # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Based on the "words" list, create a new "result" list with the lengths of these words:

def get_words_lengths(words):
    result = []

    for word in words:
        length = len(word)

        result.append(length)

    return result

words = ["one", "two", "three", "four"]
print(get_words_lengths(words))               # [3, 3, 5, 4]

# 4. Check if the elements "three" and "tow" are in the list "words" and find their indices:

words = ["one", "two", "three", "four"]

print("three" in words, ", ", words.index("three"))        # True ,  2

print("tow" in words)                                      # False
print(words.index("tow"))                                  # ValueError: 'tow' is not in list

# Creates a function that returns the longest word from a list. If the list is empty, then an "empty" string should be returned:

def get_the_longest_word(words2):
    if len(words2) == 0:
        return "empty"

    the_longest = words2[0]
    for i in range(1, len(words2)):
        if len(words2[i]) > len(the_longest):
            the_longest = words2[i]

    return the_longest

print(get_the_longest_word(["one", "two", "three", "four", "five"]))           # three

print(get_the_longest_word([]))                                                # empty

# Compare adjacent list items and display the last one alphabetically:

max = words[0]
for i in range(1, len(words)):
    if words[i] > words[i - 1]:
        max = words[i]
        print(words, ", ", max)                             # ['one', 'two', 'three', 'four'] ,  two

# Find the average value of the elements of the list "numbers". But if the list is empty, then return 0:

def get_average(numbers):

    if len(numbers) == 0:
        return 0

    total = 0
    for n in numbers:
        total += n

    return total / len(numbers)

print(get_average([1, 4, 6, 8, 15]))                        # 6.8
print(get_average([]))                                      # 0

# 5. Get a part of the "numbers" list using the "slice" function.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Take the string from index `2` to index `7`:

print(numbers[2:8])                   # [2, 3, 4, 5, 6, 7]

# Take the last 3 characters

print(numbers[-3:])                   # [7, 8, 9]

# Take the string from index `0` to index `2`:

print(numbers[:3])                    # [0, 1, 2]

# Take the string from index `1` to index `8`:

print(numbers[1:-1])                  # [1, 2, 3, 4, 5, 6, 7, 8]

# Take the string from index `1` to index `7` with the step `2`:

print(numbers[1:8:2])                 # [1, 3, 5, 7]

# Create a copy of the original list:

print(numbers[::])                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get the reversed list:

print(numbers[::-1])                  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Take the list from index `6` to index `3`, using negative step `-1`

print(numbers[6:2:-1])                # [6, 5, 4, 3]

# Take the list from index `8` to index `2`, using negative step `-2`

print(numbers[8:1:-2])                # [8, 6, 4, 2]

# 6. Number rounding.

# round "x" to the nearest whole number (up or down):

print(round(10.1),       # 10
    round(10.5),         # 10
    round(10.8),         # 11
    round(-10.1),        # -10
    round(-10.5),        # -10
    round(-10.8),        # -11
)

# round "x" down (to the nearest smaller integer):

import math

print(math.floor(10.1),  # 10
    math.floor(10.5),    # 10
    math.floor(10.8),    # 10
    math.floor(-10.1),   # -11
    math.floor(-10.5),   # -11
    math.floor(-10.8),   # -11
)

# round "x" up (to the nearest larger integer):

print(math.ceil(10.1),  # 11
    math.ceil(10.5),    # 11
    math.ceil(10.8),    # 11
    math.ceil(-10.1),   # -10
    math.ceil(-10.5),   # -10
    math.ceil(-10.8),   # -10
)

# "trim" the fractional part of "x":

print(math.trunc(10.1),  # 10
    math.trunc(10.5),    # 10
    math.trunc(10.8),    # 10
    math.trunc(-10.1),   # -10
    math.trunc(-10.5),   # -10
    math.trunc(-10.8),   # -10
)

# 7. Sort: 
# - elements of the "numbers" list in ascending order, 
# - elements of the "words" list in descending order,
# create a new list in which all elements will be displayed in reverse order (from the last element to the first).

numbers = [1, 2, 5, 1, 2, 3, 9]
numbers.sort()
print(numbers)                                  # [1, 1, 2, 2, 3, 5, 9]


words = ["apple", "circle", "banana"]
words.sort(reverse=True)
print(words)                                    # ['circle', 'banana', 'apple']


words = ["apple", "circle", "banana"]
words.reverse()
print(words)                                    # ['banana', 'circle', 'apple']

# 8. Mass production of robots is launched. In order for the work on the line to be assembled correctly, it is necessary to mark the parts. Different parts of the robot will consist of different numbers of parts. So you need to make stickers for them. Write a function "make_stickers" that takes the number "details_count" and the string "robot_part". The function should return a list of strings in the following format: {robot_part} detail #{n} (for example, Hand detail #1). Note: if details_count = 0, return an empty list.

def make_stickers(details_count: int, robot_part: str) -> list:
    listDetails = []

    if details_count == 0:
        return listDetails
    for i in range(1, details_count+1):
        listDetails += [F"{robot_part} detail #{i}"]      # or listDetails.append(f"{robot_part} detail #{i}")
    return listDetails

print(make_stickers(3, "Body"))                 # ['Body detail #1', 'Body detail #2', 'Body detail #3']
print(make_stickers(4, "Head"))                 # ['Head detail #1', 'Head detail #2', 'Head detail #3', 'Head detail #4']
print(make_stickers(0, "Foot"))                 # []

# 9. It is necessary to double the productivity of production lines. Create a function "double_power" that takes a list of "current_powers" and returns a list of doubled values.

def double_power(current_powers: list) -> list:

    double = []
    for _ in current_powers:
        double += [_*2]                         # or double.append(_ * 2)
    return double

print(double_power([100, 150, 200, 220]))       # [200, 300, 400, 440]
print(double_power([45, 34, 56, 67]))           # [90, 68, 112, 134]
print(double_power([]))                         # []

# 10. And now you need to train robots to sort boxes in the warehouse. Each box has its own unique number, and the robots learn to sort them in ascending order. But sometimes mistakes happen. Therefore, you will have to check whether the robot sorted the boxes correctly. To do this, write the "is_sorted" function, which receives a list of numbers "box_numbers" and returns "True" if all numbers are in ascending order, or "False" if not (numbers in the list can be repeated).

def is_sorted(box_numbers: list) -> bool:

    if box_numbers == []:
        return True

    copy = box_numbers[:]
    if copy == sorted(box_numbers):
        return True
    else:
        return False

print(is_sorted([1, 2, 3, 4, 5]))            # True
print(is_sorted([0, 1, 1, 1, 2]))            # True
print(is_sorted([1, 2, 11]))                 # True
print(is_sorted([5]))                        # True
print(is_sorted([]))                         # True
print(is_sorted([0, 3, 1, 2, 2, 2]))         # False
print(is_sorted([1, 11, 2]))                 # False

# 11. We complicate the work of the robot. Now he knows how to convert movement commands into the correct signal and move according to it:
# "forward" means `y + 1` (a step forward);
# "back" means `y - 1` (step back);
# "right" means `x + 1` (step to the right);
# "left" means `x - 1` (step to the left).

# But it would be great if the robot knows where it is even without GPS. To do this, implement the "get_location" function, which accepts 2 parameters:
# list of initial coordinates "coordinates" in the form [x, y];
# list with "commands" in the form ["command1", "command2", "command3" ...].

# The function should return a list of final coordinates [x, y] after movements according to commands from the "commands" list. For example, we have a list with coordinates coordinates = [2, 1] and a list with commands = ["left", "back", "back"]:
# coordinates after the first command — [1, 1] (1 step to the left);
# coordinates after the second command — [1, 0] (1 step back);
# coordinates after the third command — [1, -1] (1 step back);
# the result will be a list [1, -1].

def get_location(coordinates: list, commands: list) -> list:

    for i in range(len(commands) ) :
        if commands [i] == []:
            return coordinates

        if commands [i] == 'forward' :
            coordinates [1] += 1
        if commands [i] == 'back' :
            coordinates [1] -= 1

        if commands [i] == 'right':
            coordinates [0] += 1
        if commands [i] == 'left' :
            coordinates [0] -= 1
    return coordinates

print(get_location([0, 0], ["forward", "right"]))                                     # [1, 1]
print(get_location([2, 3], ["back", "back", "back", "right"]))                        # [3, 0]
print(get_location([0, 5], ["back", "back", "back", "right", "left", "forward"]))     # [0, 3]

# 12. Now it is necessary to increase the speed and increase the volume of production. Creates a "get_plan" function that will create a production plan for the given number of months "months". We are currently producing "current_production" of robots per month and want this number to grow by a given percentage of "percent" every month. If the number of robots per iteration is not an integer, round it down (use the "floor" function from the "math" module). In the rest, we will receive a list with goals for the coming months.

def get_plan(current_production: int, month: int, percent: int):
   
    result = []
    for i in range (month):
        current_production += math.floor(current_production*percent/100)
        result.append(math.floor(current_production))
    return result

print(get_plan(1000, 6, 35))                 # [1350, 1822, 2459, 3319, 4480, 6048]
print(get_plan(500, 3, 50))                  # [750, 1125, 1687]

# 13. The first batch of robots is ready, now they need to be tested. All robots are unique, and each has its own movement speed. In this task you need to find the smallest, largest and average speed of the robots. Write a function "get_speed_statistic" that accepts a list of robot speeds "test_results" and returns statistics in the form of a list in which:
# - the first element is the lowest speed;
# - the second element is the highest speed;
# - the third element is the average value rounded down (use math.floor).
# If the input speed list is empty, return [0, 0, 0].

from math import floor


def get_speed_statistic(test_results: list) -> list:

    speeds = []

    if test_results == []:
        return [0, 0, 0]

    speeds = [min(test_results), max(test_results), floor(sum(test_results) / len(test_results))]

    return speeds

print(get_speed_statistic([]))                         # [0, 0, 0]
print(get_speed_statistic([10]))                       # [10, 10, 10]
print(get_speed_statistic([8, 9, 3, 12]))              # [3, 12, 8]
print(get_speed_statistic([10, 10, 11, 9, 12, 8]))     # [8, 12, 10]

