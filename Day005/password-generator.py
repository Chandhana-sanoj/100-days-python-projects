letters=("A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
          "K", "L", "M", "N", "O", "P","Q", "R", "S", "T",
          "U", "V", "W", "X", "Y", "Z")

numbers=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

symbols=("!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
          "-", "_", "=", "+", "{", "}", "[", "]", "|", ";",
          ":", "'", '"', "<", ">", ",", ".", "?", "/")

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))  
nr_symbols = int(input("How many symbols would you like in your password?\n"))

import random
password_list = []

for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
    
for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
    
random.shuffle(password_list)
print(f"Your password is: {''.join(password_list)}")

# This code generates a random password based on user input for the number of letters, numbers, and symbols.
# It uses lists to store the characters and the random module to select and shuffle them.       
# The final password is printed as a single string.
