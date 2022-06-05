#PASSWORD GENERATOR
import random
print("Welcome to our password generator")
character = str("Saikayan047")
num_passwords = int(input("How many passwords"))
len_password = int(input("How long would you like your password to be?"))
print("Here are your passwords")
for password in range(num_passwords):
    password = ''
    for c in range(len_password):
        password += random.choice(character)
    print(password)
