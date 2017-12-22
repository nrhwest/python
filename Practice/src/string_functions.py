'''
Derek Banas – String Functions
'''


rand_string = "    this is an important string    "

rand_string = rand_string.lstrip() # gets rid of extra whitespace on the left of string
rand_string = rand_string.rstrip() # gets rid of extra whitespace on the right of string
rand_string = rand_string.strip() # gets rid of extra whitespace on both left and right

print(rand_string.capitalize()) # capitalizes first letter in string
print(rand_string.upper()) # sets entire string to uppercase
print(rand_string.lower()) # s entire string to lowercase

# turning a list into a string and separate te items w/ a defined separator
a_list = ["Bunch", "of", "random", "words"]
print(" | ".join(a_list))

# converts a string into a list
a_list_2 = rand_string.split()
for i in a_list_2:
    print(i)

# count how many times a string occurs within a string
print("How many is :", rand_string.count("is"))

# return the index of a matching string
print("Where is string :", rand_string.find("string"))

# replace a substring with a substring; replaces "an" with "a kind of"
print(rand_string.replace("an ", "a kind of "))


print("–––––––––––")

'''
Problem 1 – Create an acronym generator
    EX: Random Access Memory becomes RAM
    Allow the user to enter a string
    and use the functions above to convert
    that string into an acronym and convert them
    to uppercase letters


user_input = input("Convert to acronym: ") # ask user for input
user_input = user_input.upper() # convert input to uppercase

list_of_words = user_input.split() # convert the string into list
for word in list_of_words: # cycle through the list
    print(word[0], end="") # get 1st letter of word and eliminate newline
print() # print a newline
'''
print("–––––––––––")

'''
letter_z = "z"
num_3 = "3"
pi = "3.14"
a_space = " "

print("Is z a letter or number :", letter_z.isalnum()) # checks if string contains ONLY characters and numbers
print("Is z a letter :", letter_z.isalpha()) # checks if string contains ONLY letters
print("Is 3 a number :", num_3.isdigit()) # checks if string contains ONLY numbers ** not true for floats
print("Is z lowercase :", letter_z.islower()) # checks if string contains ONLY lowercase
print("Is z uppercase :", letter_z.isupper()) # checks if string contains ONLY uppercase
print("Is space a space :", a_space.isspace()) # checks if string contains ONLY spaces

def isfloat(str_val): # creating a function/method to check if string is float
    try: # try to convert string to float
        float(str_val)
        return True # if conversion succeeds return True
    except ValueError: # catch exceptions
        return False # if conversion fails return False

print("Is pi a float :", isfloat(pi))
'''
print("–––––––––––")

'''
Problem 2 – Implement Caesar's cypher
    Pass a message that you want encrypted
'''

# A - Z, 65 - 90
# a - z, 97 – 122
# ord(your_letter)
# chr(your_code)

message = input("Enter a message to encrypt : ") # receive message to encrypt
key = int(input("How many characters should we shift (1 - 26) : ")) # receive key to shift
secret_message = "" # prepare secret message

for char in message: # cycle through each character in message
    if char.isalpha(): # checks if the character is a letter
        char_code = ord(char) # get the character code and add the shift amount
        char_code += key
        if char.isupper(): # if uppercase, compare to uppercase unicodes
            #print(char)
            if char_code > ord('Z'): # if bigger than Z, subtract 26
                 char_code -= 26
            if char_code < ord('A'): # if smaller than A, add 26
                char_code += 26
        else:  # if lowercase, compare to uppercase unicodes
             if char_code > ord('z'):
                 char_code -= 26
             if char_code < ord('a'):
                 char_code += 26
        secret_message += chr(char_code)
    else: # if not a letter leave character alone
        secret_message += char
print("Encrypted messge :", secret_message)

key = -key
orig_message = ""
for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                 char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
             if char_code > ord('z'):
                char_code -= 26
             if char_code < ord('a'):
                 char_code += 26
             orig_message += chr(char_code)
    else:
        orig_message += char
print("Decrypted messge :", orig_message)
