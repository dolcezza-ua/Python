# 1. Create a variable `item`. 
# Assign the number 5 to the variable `item`.
# Print `item` to the console.

item = 5
print(item)

# 2. Create a variable `x`. 
# Assign the None to the variable `x`.
# Print the `x` data type to the console as "type of x is: " data type x.
# Check if variable x is string, number, float, boolean.

x = None
print(" type of x is: ", type(x))
print(isinstance(x, str))
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, bool))

# 3.  Create a variable `name`and `age`. 
# Assign the string `Bob` to the variable `name` and the number 25 to the variable `age`.
# Display message (the addition of `name`, " is " and `age`) to the console.

name = "Bob"
age = 25
message_1 = name + " is " + str(age)
message_2 = f"{name} is {age}"
print(message_1)
print(message_2)



