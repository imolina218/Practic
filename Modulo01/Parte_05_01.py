# employee_dict = {"name": name, "last name": last_name["base salary": base_salary,
#                                            "Afap": afap, "start date": start_date, "children amount": children_amount]}
# employees = {}

# name = ""
# last_name = ""
# base_salary = ""
# afap = ""
# start_date = ""
# children_amount = ""


def employee_input():

    name = input("Please enter your first name : ")
    while name.isalpha() == False:
        name = input("Invalid input. Please enter your first name. (only letters)")

    last_name = input("Please enter your last name: ")
    while last_name.isalpha() == False:
        last_name = input("Invalid input. Please enter your last name. (only letters)")

    base_salary = input("Please enter your base salary: ")
    while base_salary.isalnum() == False:
        base_salary = input("Invalid input. Please enter your base salary.")
        base_salary = float(base_salary)

    afap = input("Please enter your AFAP company: ")
    start_date = input("Please enter the date that you start working in this company (example: 12/11/2000): ")
    start_date = str(start_date)

    children_amount = input("Please enter how many children you have: ")
    while children_amount.isdigit() == False and children_amount != int:
        children_amount = input("Invalid input. Please enter how many children you have (only numbers): ")
        children_amount = int(children_amount)

    employee_dict = {"name": name, "last name": last_name["base salary": base_salary,
                                                "afap": afap, "start date": start_date,
                                                "children amount": children_amount]}

    print(employee_dict)


employee_input()









