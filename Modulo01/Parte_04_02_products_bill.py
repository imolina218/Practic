# Create a program that have a list of products by code.
# Then the user can choose the product and the amount, the option to choose more than
# one product needs to be available.
# Once the user doesn't want to enter any more products the program will print the
# bill with all the product/s and the quantity


def product_shopping():
    confirmation = True
    bill_total = ""
    total_amount = 0
    bill_total_total = "Total amount to pay:..................${}".format(total_amount)
    while confirmation:
        print("Welcome to the store. This are our products: ")
        print("> Monitor.........$120\n> Motherboard.........$200\n> Mouse.........$30\n> Ram.........$20\n"
              "> Coolers.........$5\n> Keyboard.........$80\n> Speakers.........$60\n> Router.........$45")

        products = {"monitor": 120, "motherboard": 200, "mouse": 30, "ram": 20, "coolers": 5, "keyboard": 80,
                    "speakers": 60, "router": 45}
        select_product = input("Enter the name of the product that you want to buy: ")
        select_product = select_product.lower()
        amount_product = input("Now enter the amount that you want:")
        amount_product = int(amount_product)

        price = (products[select_product] * amount_product)
        confirmation = input("Do you want to buy more products?").lower()
        print("\n\n")

        bill = "Product: {} | Amount: {} | Total: ${}\n".format(select_product, amount_product, price)
        bill_total += bill
        total_amount += price
        if confirmation in "yes":
            confirmation = True
        else:
            confirmation = False
    print(bill_total)
    print(bill_total_total)


product_shopping()



