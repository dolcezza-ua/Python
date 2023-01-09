# 1. Find out the length of each string (the number of characters in it) using the `len` function, and print the shorter word.

a = "Michael"
b = "Max"

print(len(a))
print(len(b))

shortest = a if len(a) < len(b) else b
print(shortest)

# 2. Get a single character in the string by its index:

full_name = "Gaius Julius Caesar"

print(full_name[0])                              # Get the first character in the string

print(full_name[18])                             # Get the last character in the string
print(full_name[len(full_name) - 1])             # Get the last character in a string using the `len` operator.
print(full_name[- 1])                            # Get the last character in a string using a negative index.

# 3. Print all characters in the string in two different ways using a `for' loop.

info = "My name is Olha."

for i in range(len(info)):
    print(info[i])


for char in info:
    print(char)

# Print all characters in the string and their indices in two different ways using a `for' loop.

for i in range(len(info)):
    print(i, ": ", info[i])


for index, char in enumerate(info):
    print(index, ": ", char)

# Using a loop, count the number of spaces in the string.

spaces_count = 0

for char in info:
    if char == " ":
        spaces_count += 1

print(spaces_count)  # 3

# 4. Check if "part" is part of "text" and print the index of the first occurrence in two different ways.

text = "a bc de bc"
part = "bc"

print(                           
    part in text,
    text.index(part),            # True 2 2
    text.find(part)
)

# Check if "part" is part of "text" and print the index of the last occurrence in two different ways.

print(                           
    part in text,
    text.rindex(part),           # True 8 8
    text.rfind(part)
)

# Check if "part" is part of "text"; check if "part" is the start and end of "text".

print(                           
    part in text,
    text.startswith(part),       # True False True
    text.endswith(part)
)

# 5. Convert characters of the string.

message = "my name is Olha."

# convert only the first character of the string to uppercase

capitalize_message = message.capitalize()
print(message.capitalize())                    # My name is olha.

# convert all characters of the input string "message" to uppercase

upper_message = message.upper()
print(message.upper())                         # MY NAME IS OLHA.

# convert all characters of the input string "message" to lowercase

lower_message = message.lower()
print(message.lower())                         # my name is olha.

# 6. Check if the `model` string contains the `search` substring, using case-insensitive search.

model = "Apple Iphone 14"
search = "iph"

normalized_model = model.lower()             
normalized_search = search.lower()           # or normalized_model = model.upper() and normalized_search = search.upper()

if normalized_search in normalized_model:
    print("Found ! ")

# Create a "search" function that checks whether the "text" string contains the "part" substring using a case-insensitive search.

def search(text, part):
    normalized_text = text.lower()             # or normalized_text = text.upper()
    normalized_part = part.lower()             # or normalized_part = part.upper()
    return normalized_part in normalized_text

print(search("Apple Iphone 14!", "iph"))       # True
print(search("Hello, world!", "h"))            # True
print(search("Long-long text", "T"))           # True

# 7. Create a "find_model" function that checks whether the "model" string  contains the "search" substring  using a case-insensitive search and interactive "input" programs.

model = "Apple Iphone 14"

def find_model(search_text: str) -> None:
    is_found = search_text.lower() in model.lower()

    if is_found:
        print("Found ! ")

search = input("Enter search text: ")
find_model(search)

# modify the above function so that the introduction with the help of the interactive program "input" is performed repeatedly

def find_model(search_text: str) -> None:
    is_found = search_text.lower() in model.lower()

    if is_found:
        print("Found ! ")

while True:
    search = input("Enter search text: ")
    find_model(search)

# 8. Get a part of the "txt" string using the "slice" function.

txt = "0123456789"

sl = slice(1, 5)       # or print(txt[1:5]) or print(txt[1:5:1])
print(txt[sl])

# Take the string from index `0` to index `8`

print(txt[:-1])        # or print(txt[0:9])

# Take the last 3 characters

print(txt[7:])         # or print(txt[-3:])

# Take the string from index `5` to index `8`

print(txt[-5:-1])      # or print(txt[5:9])

# Take characters with the step `2`

print(txt[::2])

# Get the reversed string

print(txt[::-1])       # "9876543210"

# Take the string from index `6` to index `3`, using negative step `-1`

print(txt[6:2:-1])     # "6543"

# Take the string from index `8` to index `2`, using negative step `-2`

print(txt[8:1:-2])     # "8642"

# 9. Convert the number "n" to a string in three different ways.

n = -123

first_string = str(n)
second_string = "%s" % n
third_string = f"{n}"

print(first_string)    # -123
print(second_string)   # -123
print(third_string)    # -123

# Check the data type of first_string, second_string and third_string using the type function.

print(type(first_string))     # <class 'str'>
print(type(second_string))    # <class 'str'>
print(type(third_string))     # <class 'str'>

# 10. The new boss, as it turns out, just hates vowels, so you need to remove them from all documentation. Create a function "remove_vowels" (in two different ways) that takes the string "document" and returns a new string with all vowels removed (vowels are `aeiouy' in any case).

def remove_vowels(document: str) -> str:

    result_document = ""
    vowels = "aeiouy"
    for i in range(0, len(document)):
        if document[i].lower() not in vowels:
            result_document += document[i]
    return result_document

print(remove_vowels("captain"))             # cptn
print(remove_vowels("I like my boss"))      #  lk m bss
print(remove_vowels("350 euro"))            # 350 r



def remove_vowels(document: str) -> str:
    result_document = ""
    vowels = "aeiouy" + "aeiouy".upper()
    for letter in document:
        if letter not in vowels:
            result_document += letter
    return result_document

print(remove_vowels("captain"))              # cptn
print(remove_vowels("I like my boss"))       #  lk m bss
print(remove_vowels("350 euro"))             # 350 r

# 11. Create a function "make_abbr" that takes a string of words "words" and returns an abbreviation from them in uppercase. The string "words" contains one or more words separated by a space. And if "words" does not contain any character, return an empty string.
# Example:
# make_abbr("national aeronautics space administration")             # "NASA"
# make_abbr("central processing unit")                               # "CPU"
# make_abbr("simplified molecular input line entry specification")   # "SMILES"

def make_abbr(words: str) -> str:

    abbr = ""
    for i in words.split():
        abbr += i[0]
    return(abbr.upper())

print(make_abbr("national aeronautics space administration"))            # NASA
print(make_abbr("central processing unit"))                              # CPU
print(make_abbr("simplified molecular input line entry specification"))  # SMILES

# 12. Create a function "decrypt_message" that takes the string "message" and returns a new string where the characters from "message" are in reverse order.

def decrypt_message(message: str) -> str:

    return message[::-1]

print(decrypt_message("!!!reeb gniknird ekil eW"))   # We like drinking beer!!!
print(decrypt_message("cimednap surivanoroc A"))     # A coronavirus pandemic

# 13. Create a function "happy_birthday" that will read the string "name" using the "input" function and output a greeting string in the format "Happy birthday, {name}!".

def happy_birthday() -> None:

    name = input("What's your name?")
    print(f"Happy birthday, {name}!")

happy_birthday()

# 14. Create a "parity_checker" function that: reads the number entered by the user using the "input" function; outputs the string "Even" if the number is even, or the string "Odd" if the number is odd. In the "input" function, send the message "What number do you want to check?", so that the user understands what information needs to be entered (if the user entered "0" - output the line "Even"; the function should not return anything, so you only need to use print).

def parity_checker() -> None:
    number = int(input("What number do you want to check?"))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

parity_checker()

# 15. It is a program for collecting statistics from webinars. It sends data to the server in the form of a string "111001010111011", where 1 is the student who understood the topic, and 0 means that he did not. It would be useful to understand what percentage of students learned the material, that is, how effective the webinar was. To do this, create the "get_success_rate" function, which accepts the string "statistic" and returns the percentage of students who understood the material, rounded to the nearest integer (use the round function). If the input line is empty, return 0.

def get_success_rate(statistics: str) -> int:

    message = ""

    if len(statistics) != 0:
        for i in range(len(statistics)):
            if statistics[i] == "1":
                message = message + statistics[i]
        result = len(message) * 100 / len(statistics)
        return round(result)
    return 0

print(get_success_rate("1000000000"))     # 10
print(get_success_rate("1100"))           # 50