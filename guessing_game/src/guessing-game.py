'''
guessing-game.py
Nathan West
January 4, 2018

Guess a number between 1 and 1000
'''
import random

def main():
    print "Guess a number between 1-100"
    randomNumber = random.randint(1, 10)
    found = False

    while not found:
        guess = input("Enter: ")
        if guess == randomNumber:
            print("Correct!")
            found = True
        else:
            print("Guess again.")

if __name__ == "__main__":
    main()
