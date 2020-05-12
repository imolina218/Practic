# Create a program that ask the user to input an amount of dollars an interest rate
# and a certain amount of years.
# Then print out how much money will have with the interest rate in the amount of years
# and also show the interest rate profits.


def calculate_interest_rate():
    amount = input("Please enter the amount of dollars that you want to deposit: ")
    amount = float(amount)
    interest = input("And now enter the interest rate that you are looking for: ")
    interest = float(interest)
    years = input("Finally, now please enter the total years that you want to deposit your dollars. ")
    years = int(years)
    total_interest = interest*years
    total_profits = (amount*total_interest)//100
    total_amount = (amount*total_interest)//100 + amount

    print("You deposit $${0} with an {1}% year interest for {2} years.".format(amount, interest, years))
    print("The total money to withdraw in {0} years is going to be ${1} with {2}% "
          "of interest rate with a profit of ${3} dollars.".format(years, total_amount, total_interest, total_profits))


calculate_interest_rate()







