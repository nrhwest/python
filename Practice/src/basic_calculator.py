'''
Enter Calculations: 5 * 6
print 5 * 6 = 30
'''

# Store the uesr input of 2 numbers and the operator
num1, operator, num2 = input('Enter Calculation: ').split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based on addition
# Print result
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print(':-P')
