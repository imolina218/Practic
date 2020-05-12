# Create a program that shows a catalog of movies category with a price
# and the interest of each category every day that pass.
# Then ask the user to choose a genre and input the amount of days of rent.
# Finally print the category and the total to pay for the genre and the interest.


def choose_category():
    print("This is our movie category with their respective prices.")
    print("Category\t\t\t\tprice\t\t\t\tinterest(per day)")
    print("Favorites\t\t\t\t$1.5\t\t\t\t$0.5")
    print("New\t\t\t\t\t\t$2.0\t\t\t\t$1.0")
    print("Premieres\t\t\t\t$2.5\t\t\t\t$1.5")
    print("Super premieres\t\t\t$3.0\t\t\t\t$1.8")

    categories = {"favorites": 1.5, "new": 2.0, "premiers": 2.5, "super": 3.0}
    categories_interest = {"favorites": 0.5, "new": 1.0, "premiers": 1.5, "super": 1.8}

    user_input = input("Please enter the movie category that you want:")
    user_input = user_input.lower()
    user_days = input("Now enter the amount of days that you want to rent it: ")
    user_days = int(user_days)

    interest_day = categories_interest[user_input] * user_days
    total_amount = (categories[user_input] + interest_day)
    print("The total is ${} with an interest of ${} per day.".format(total_amount, categories_interest[user_input]))


choose_category()

