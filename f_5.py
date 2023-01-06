# 1. Print happy birthday greetings up to 35 years old for every odd age.

for age in range(1, 35, 2):
    print(f"Happy birthday! I am {age}")

# 2. Create a program that counts how many times a given number is divisible by number 2 without a remainder.
# Use operator WHILE.

num = 123400
count = 0

while num % 2 ==0:
    num //= 2
  # print(num)
    count +=1

print(count)

# 3. What will be the result of this code?

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

Answer: 1 2 3 will be printed

# 4. Once, the presenter at the wedding decided to entertain the guests and established a rule: each guest makes a toast, and everyone present drinks to the health of the young.
# Example:
# when the first guest arrives, he drinks alone;
# when the second one comes, they drink together;
# the third - the three of them drink and so on.

# If there are 5 guests, then you will need 15 servings (1 + 2 + 3 + 4 + 5).
# If 10, then 55 portions (1 + 2 + 3 + ... + 10).

# Implement the function `get_drinks`, which accepts `number_of_guests` - how many guests there will be, and returns the required number of servings.

def get_drinks(number_of_guests: int) -> int:

    amount = 0

    for i in range(0, number_of_guests +1, 1):

        amount = amount + i
      # print(amount)
    return amount
print(get_drinks(5))
print(get_drinks(10))

# 5. In Mate bank, it is possible to put money on a deposit at a certain percentage and get a profit after some time.
# For example, if we put 10,000 for 3 years at 4% per annum, we will get:
# first year: 10000 + 4% = 10400 (10000 + 10000 * 0.04);
# second year: 10400 + 4% = 10816 (10400 + 10400 * 0.04);
# third year: 10816 + 4% = 11248.64 (10816 + 10816 * 0.04);
# net profit: 11248.64 - 10000 = 1248.64.
# Your task: write the function calculate_profit, which accepts 3 parameters:
# amount — the initial amount that we deposit;
# percent — annual interest rate;
# period — the number of years (time for which money is deposited).
# The function should calculate and return the amount of net profit for all time.
# Please note: if amount, percent or period is equal to 0, the function must return 0.
calculate_profit(1000, 5, 1)  # 50

from typing import Union

def calculate_profit(amount: int, percent: Union[float, int], period: int) -> Union[float, int]:
    profit = 0
    if period == 0:
        return profit

    for period in range(1, period+1, 1):
        profit = profit + (amount+profit)*percent/100

    return profit
print(calculate_profit(1000, 5, 1))