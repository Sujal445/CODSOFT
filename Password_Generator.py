# Task 2 password generator
# importing random module
import random

# list of alphabet
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# list of numbers
numbers = ['1','2','3','4','5','6','7','8','9','0']

# list of some symbols
symbols = ['@','#','$','&','*','+','_','-','<','>']

# empty list
password = []

print("\nWellcome to the PASSWORD GENERATOR\n")

# inserting random letters in password

letterLength = int(input("Enter a length of letters in password : \n"))

for i in range(0,letterLength):
    letter = random.choice(letters)
    password += letter

# inserting random numbers in password

numberLength = int(input("Enter a length of numbers in passwoad : \n"))

for i in range(0,numberLength) :
    number = random.choice(numbers)
    password += number

# inserting random symbols in password

symbolsLength = int(input("Enter a length of symbols in password : \n")) 

for i in range(0,symbolsLength):
    symbol = random.choice(symbols)
    password += symbol

# shuffling the letters of password
random.shuffle(password)

# printing password6
print("Generated Password is : ")
for letter in password:
    print(letter,end='')