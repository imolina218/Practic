# Create a simple version of the "Master mind" game, that consist on guessing a random
# chain of numbers with a random length that  goes from 2 to 9 and the user have to guess
# the the numbers in the random generated chain. The program have to tell the user the length of the
# generated chain.
import random
game = True
while game:
    unknown = []
    guessed = []
    score = 0
    for i in range(random.randint(2, 10)):
        unknown.append(random.randint(0, 9))
    unknown = str(unknown)
    print("Welcome to the simplify version of Master Mind.")
    print("The program is going to generate a chain of numbers with a random length\n "
          "that goes from 1 to 9. The length will be provide and you'r going to guess\n"
          " the numbers in the chain. (NO COMAS AND LETTERS ONLY NUMBERS FROM 0 TO 9)\n")
    print("The length of the chain is {}.".format(len(unknown)))
    guess = input(":")
    for i in guess:
        if i in unknown:
            score += 1
            guessed.append(i)
    print("You guessed {0} numbers the number/s are {1}".format(score, guessed))
    break




