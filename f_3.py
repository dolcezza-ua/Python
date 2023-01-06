# 1. Print information "Access granted" if age = 18, otherwise print information "Access denied".

age = 19
has_access = age == 18

print("Variable has_access:", has_access)

if has_access:
    print("Access granted")
else:
    print("Access denied")

# 2. Display "Access granted" if age is not 18, otherwise display "Access denied".

age = 18
has_access = age != 18

print("Variable has_access:", has_access)

if has_access:
    print("Access granted")
else:
    print("Access denied")

# 3. Display information "Can buy: True" if the money in the wallet is not less than the price of the goods and the age is at least 18 years old, otherwise output "Can buy: False"
# Use operator AND.

cash_in_wallet = 50
price = 40

age = 25
age_limit = 18

has_enough_money = cash_in_wallet >= price
is_allowed = age >= age_limit

can_buy = has_enough_money and is_allowed
print("Can buy:", can_buy)

# 4. Display information "Can buy: True" if the money in the wallet or on the card is not less than the price of the goods, otherwise display "Can buy: False". 
# Use operator OR.

cash_in_wallet = 30
cardAmount = 50
price = 40

has_enough_cash = cash_in_wallet >= price
can_pay_by_card = cardAmount >= price

can_buy = has_enough_money or can_pay_by_card
print("Can buy:", can_buy)