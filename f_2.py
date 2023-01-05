# 1. Print information (perimeter and square) for 5x8, 3x10, 6x9 rectangles using the function

def print_rectangle_info(a, b):
    perimeter = 2*a + 2*b
    square = a*b

    print("Rectangle: ", a, " x ", b)
    print("Perimeter: ", perimeter)
    print("Square: ", square)
    print("-----------------------------------------------------")
    
# Rectangle 5x8
print_rectangle_info(5, 8)

# Rectangle 3x10
print_rectangle_info(3, 10)

# Rectangle 6x9
print_rectangle_info(6, 9)

# 2. Print information (number of floors) for a small house (number of floors from 1 to 5) and for a big house (number of floors more than 5) using the function.

def build_house(number_of_floors):
    house = f"{number_of_floors}-- floors house"
    return house

small_house = build_house(2)
big_house = build_house(9)

print(small_house)
print(big_house)

# 3. Create a greeter function that accepts a `name' parameter.
# Using the `name` parameter, return from the function a greeting string of the following format: Hi, {name}!.
# P.S.: you can use concatenation or interpolation to format the string.

def greeter(name):
    massage = f"Hi, {name}!"
    print(massage)
    return massage

greeter("Max")

# 4. Create a `greeter` function that:
# - takes parameters `name` and `part_of_the_day`
# - returns a string by pattern: "Good night, Paul!"

def greeter(name, part_of_the_day):
    message = f"Good {part_of_the_day}, {name}!"
    print(message)
    return message

greeter("Max", "morning")

# 5. Create a function with an `age` parameter that shows whether the person is an adult or not.

def is_adult(age: int) -> bool:
    return age >= 18

print(is_adult(15))  # False
print(is_adult(32))  # True