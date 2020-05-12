# Write a program that asks for the total amount of the purchase from the store.
# If the amount is less than $100.00 the program will notify that the discount doesn't apply
# But if the amount is equal or more than $100.00 the program will choose a random discount out of 5
# At the end the program have to notify the consumer the discount and the total less the discount
import random


def discount_game():
    amount = input("Please enter the total amount to see if you get a discount.")
    amount = float(amount)
    discount = ([0, 10, 25, 30, 75])

    if amount < 100:
        print("Sorry, to play this game you need to have $100.00 or more in your ticket.")

    while amount >= 100:
        print("You enter the game")
        ball_select = random.choice(discount)
        final_amount = amount - (ball_select * amount)/100
        print("You have a %{0} discount off ${1} the final amount to pay is ${2}".format(ball_select, amount,
                                                                                         final_amount))
        break


discount_game()









