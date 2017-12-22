'''
Derek Banas - Learn to Program 3: Math, Strings, Exception Handling
'''


while True: # asks for input repeatedly

    try: # try to receive a number
        number = int(input("Enter a number: ")) # user enters number
        break # stops the while loop
    except ValueError: # catches if user does not enter a number
        print("You didn't enter a number")
    except: # catches any error program throws
        print("An unknown error occurred!")

print("Thank you for entering a number")


print("–––––––––––––––")

'''
Problem 1 –
    Implement a do-while loop.
    Create a guessing game in which the user
    must enter a number between 1 and 10
'''

import random
number = random.randrange(1,10)

while True:
    try:
        guess = int(input("Guess a number 1-10: "))
        if (guess != number):
            print("Enter try again!")
            continue
        else:
            print("You guess correctly!")
            break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error ocurred")

print("–––––––––––––––")

import math # imports math class w/ functions

print("ceil(4.4) = ", math.ceil(4.4)) # rounds up
print("floor(4.4) = ", math.floor(4.4)) # rounds down
print("fabs(4.4) = ", math.fabs(-4.4)) # absolute value
print("factorial(4) = ", math.factorial(4)) # Factorial – 4! = 1 * 2 * 3 * 4
print("fmod(5,4) = ", math.fmod(5,4)) # returns the remainder of division
print("trunc(4.2) = ", math.trunc(4.2)) # receives a float and return an int
print("pow(2,2) = ", math.pow(2,2)) # returns x^y (2^2)
print("sqrt(4) = ", math.sqrt(4)) # returns the square root
print("math.e = ", math.e) # exponential
print("math.pi = ", math.pi) # pi - 3.14
print("exp(4) = ", math.exp(4)) # returns e^x (e^4)
print("log(20) = ", math.log(20)) # return the natural log
print("log(1000,10) = ", math.log(1000,10)) # defines the base
print("log10(1000) = ", math.log10(1000)) # automatic base of 10

# Trig functions
# There are also sin, cos, tan, asin, acos, atan, etc..
print("–––––––––––––––")

from decimal import Decimal as D
# from references the methods/functions that are inside the decimal
# D creates an alias, which allows us to avoid calling methods with the same name

sum = D(0)
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print("Sum = ", sum)
print(".1 + .1 + .1 - .3 = ", .1 + .1 + .1 - .3)


print("–––––––––––––––")


print(type(3)) # type() identifies the data type a variable
print(type(3.145234235))
print(type("Hello"))

sample_string = "This is a very important string"
print(sample_string[15]) # grabs the letter at index 15
print("Length of string = ", len(sample_string)) # returns the length of the String
print(sample_string[0:4]) # splits the String, only printing from index 0 to 4
print("Hello " * 5) # prints "Hello" 5 times
number_str = str(4) # converts the int into a String

for char in sample_string: # loops through String, print out each letter of string
    print(char)

for x in range(0, len(sample_string) - 1, 2): # loops through the String, print out pairs of the letters
    print(sample_string[x] + sample_string[x+1])

# A - Z, 65 - 90
# a - z, 97 - 122
print("A = ", ord("A")) # ord() returns the unicode for letters and symbols
print("65 = ", chr(65)) # chr() converts a integer into it's corresponding unicode letter/symbol

print("–––––––––––––––")

'''
Problem 2 –
    Receive an uppercase string, then
    hide it's meaning by turning it into a string of unicode,
    then translate it from unicode back to it's original meaning
'''

norm_string = input("Enter a string : ") # ask for input
secret_code = "" # initialize secret code
for char in (norm_string): # cycle through each char of input
    secret_code += str(ord(char) - 23) # store each character code in secret_code
print(norm_string, "in unicode is", secret_code) # print results

norm_string = ""
for x in range(0, len(secret_code) - 1, 2): # cycle through secret_code 2 at a time by increment by 2
    char_code = secret_code[x] + secret_code[x + 1] # grab the 1st and 2nd for the digit number
    norm_string += chr(int(char_code) + 23) # convert the code into characters and add them to a new string
print("From unicode -", secret_code, "- to original string:", norm_string) # print results

print("–––––––––––––––")
