# 1. Print "Baby" if the age is under 3 years old;  print "Toddler" if age is more than 3 years old and less than 7;  print "Child" if age is more than 7 years old, but less than 18;  output "Adult" if age is more than or equal to 18 years old.

age = 23

if age >= 18:
    print("Adult")
elif age > 7:
    print("Child")
elif age > 3:
    print("Toddler")
else:
    print("Baby")

# 2. Write a program that calculates the amount a customer who rents an apartment must pay.  Rent for the first three days - 50 eur per day, from 4 to 7 days - 40 eur per day and more than 7 days - 30 eur per day.

short_term_cost = 50   # days 1-3
middle_term_cost = 40  # days 4-7
long_term_cost = 30    # days 8-...

def get_rental_price(number_of_days):
    if number_of_days <= 3:
        return number_of_days * 50

    days_left = number_of_days - 3

    if days_left <= 4:
        return 3*50 + days_left *40

    days_left = number_of_days - 7
    
    return 3 * 50 + 4 * 40 + days_left * 30

print(
    get_rental_price(2),  # 2 * 50 = 100
    get_rental_price(5),  # 3 * 50 + 2 * 40 = 230
    get_rental_price(10)  # 3 * 50 + 4 * 40 + 3 * 30 = 400
)

# 3. Print "Adult" if the age is greater than or equal to 18, otherwise print "Child". Use a conditional operator.

age = 5
message = "Adult" if age >= 18 else "Child"
print(message)

# 4. By law, only adults can buy alcoholic beverages.
# Create a function `can_buy_beer` that takes the integer age as a parameter:
# - if `age` is greater than or equal to 18, the function will return the string "You can buy beer";
# - otherwise, the function will return the string "You can not buy beer".

def can_buy_beer(age: int) -> str:
    if age >= 18:
        return "You can buy beer"

    return "You can not buy beer"

print(can_buy_beer(13))
print(can_buy_beer(18))

# 5. Implement the get_tips_rating function, which accepts the tip amount and returns a rating string according to the amount left:
# - terrible, if amount is 0 eur;
# - poor, if the amount is from 1 to 10 eur inclusive;
# - good, if the amount is from 11 to 20 eur inclusive;
# - great, if the amount is from 21 to 50 eur inclusive;
# - excellent, if the amount is more than 50 eur.

def get_tips_rating(amount: int) -> str:
    if amount == 0:
        return "terrible"
    if amount <= 10:
        return "poor"
    if amount <= 20:
        return "good"
    if amount <= 50:
        return "great"
    return "excellent"

print(get_tips_rating(7))
print(get_tips_rating(35))

# 6. Create a function `calculate_taxes` that takes an integer `income` and returns the tax you will pay. The amount of tax depends on your income:
#  up to 1000 eur inclusive — tax of 2% of income;
#  from 1001 eur to 10000 eur inclusive — a tax of 3% of the income;
#  more than 10,000 eur — a tax of 5% of the income.

def calculate_taxes(income: int) -> float:
    if income <= 1000:
        return income * 0.02
    if income <= 10000:
        return income * 0.03
    return income * 0.05

print(calculate_taxes(980))
print(calculate_taxes(7000))
print(calculate_taxes(20000))

# 7. Create a function `get_largest_expression_result` that accepts 2 numbers: a and b. This function should compare the results of the following calculations and return the largest of them (numbers a and b can be negative,a and b are not equal to zero):
# a + b
# a - b
# a * b
# a / b

def get_largest_expression_result(a, b):
    result = a + b
    if a - b > result:
        result = a - b
    if a * b > result:
        result = a * b
    if a / b > result:
        result = a / b
    return result

print(get_largest_expression_result(10, 5))
print(get_largest_expression_result(10, -5))
print(get_largest_expression_result(-6, -6))
