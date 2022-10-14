
import random


letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy mode

password = ""

for char in range(1, nr_letters +1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

# Hard Mode

# Flowchart for Hard
# - when we get the password the first time,
# - feed the letters into a dispoasble array and
# - Run through the array and reconstitute password using
# -  random.choice##

tempArray = []
for char in password:
    tempArray.append(char)

print(tempArray)

password = ""

for char in range(1, len(tempArray) + 1):
    randChar = random.choice(tempArray)

    password += randChar
    tempArray.remove(randChar)

# or we could have just used random.shuffle(list) instead

print(tempArray)
print(password)