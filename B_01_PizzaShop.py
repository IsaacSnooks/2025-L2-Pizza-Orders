import pandas
from tabulate import tabulate
from datetime import date
import math
# Importing numpy package
import numpy as np


# Functions go here
def make_statement(statement, decoration):
    """Emphasis headings by adding decoration at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no_check(question):
    while True:
        response = input(question).lower()

        # checks user response, question repeats if users don't enter y/n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no\n")


def instructions():
    make_statement("Instructions", "❕")

    print('''

For each pizza wanted type...
- The pizzas name
- How many pizzas
- The size
- Extra toppings

The program will record the amount of pizzas, the types of pizzas, the size of pizzas, the extra toppings, and the cost.

Once you have either bought 5 pizzas or wish to finish your order
the program will display the information on your pizza and write the data to a text file. 
Enter corresponding number for items on menu to purchase.

    ''')


def string_check(question, valid_answer, num_letters=1):
    """Checks that users enter the full word or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answer:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answer}")


def menu():
    make_statement("Menu", "📃")

    print('''

Pizzas: 
1.Peperoni
2.Meat Lovers
3.Hawaiian
4.Cheese
5.Margarita 



Extra Toppings:
1. Cheese
2. Ham
3. Pineapple
4. Bacon
5. Chicken

All Extra Topping $1

       ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank. Please try again.\n")


def num_check(question, low, high):
    """Checks users enter an integer / float that us higher than zero (or the optional exit code)"""

    while True:

        error = f"Enter a number between {low} and {high}"

        # check datatype is correct and that number is more than zero
        try:

            response = int(input(question))

            # check for valid number
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type, how_many=1):
    """Gets variable / fixed expenses and outputs panda (as a string) and a subtotal of the expenses"""

    # Lists for panda
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    # defaults for fixed expenses
    amount = how_many  # how_many defaults to 1
    how_much_questions = "How much? $"

    # loop to get expenses
    while True:
        # Get item name and check it's not blank
        item_name = not_blank("Item Name: ")

        # check users enter at least one variable expense
        if exp_type == "variable" and item_name == "xxx" and len(all_items) == 0:
            print("Oops - you have not entered anything. "
                  "You need at least 1 items.")
            continue

        # end loop when users enter exit code
        elif item_name == "xxx":
            break

        # Get variable expenses item amount <enter> defaults to number of products being made.
        if exp_type == "variable":
            amount = num_check(f"How many <enter for {how_many}> ", "integer", "")

        # Allows users to pus <enter> to default to number of items being made
        if amount == "":
            amount = how_many

        how_much_question = "Price for one? $"

        # Get price for item (question customised depending on expense type).
        price_for_one = num_check(how_much_question, "float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # Calculate Row Cost
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # Apply currency formatting to currency columns.
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    # make expense frame into a string with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys',
                                  tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    # return all items for now so we can check loop.
    return expense_string, subtotal


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


def round_up(amount, round_val):
    """Rounds amount to desired hole number"""
    return int(math.ceil(amount / round_val)) * round_val


def profit_goal(total_costs):
    """Calculates profit goal work out profit goal and total sales required"""
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%): ")

        # check if first character is $
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no_check(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars?")

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "%"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no_check(f"Do you mean {amount}%? , y / n: ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Main routine goes here

# Initialise variables...

MAX_PIZZAS = 5
MAX_PER_ORDER = 3
total_pizza_made = 0
total_cost_pizza = 0



size_options = ["large", "medium", "small"]

pizza_list = [
    "Peperoni", "Meat Lovers", "Hawaiian", "Cheese", "Margarita"
]
toppings_list = [
    "Cheese", "Ham", "Pineapple", "Bacon", "Chicken"
]

pizza_size_price = [5, 7.50, 10]
extra_topping_price = [1]

cust_pizza = []
cust_pizza_size = []
cust_pizza_cost = []
cust_extra_toppings = []

print(make_statement("Isaacs Pizza Shop", "🍕"))

print()
want_instructions = yes_no_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

want_menu = yes_no_check("Do you want to see the menu? ")

if want_menu == "yes":
    menu()

print()

while True:

    max_remaining = MAX_PIZZAS - total_pizza_made

    if max_remaining == 0:
        print("you have reached maximum pizzas allowed")
        break

    max_allowed = min(MAX_PER_ORDER, max_remaining)

    # Get product details
    pizza_type = num_check("Which pizza? ", 1, 5)
    quantity_made = num_check(f"Quantity being made (max {max_allowed}): ", 1, max_allowed)

    total_pizza_made += quantity_made

    if total_pizza_made >= MAX_PIZZAS:
        print("max pizzas brought")
        break

    print(f"You have purchased {quantity_made} {pizza_list[pizza_type - 1]} pizzas!")

    # Add pizza to customer list
    cust_pizza.append(pizza_list[pizza_type - 1])

    print("Sizes and Prices for Pizzas: Large ($10) Medium ($7.50) Small ($5)")

    pizza_size = string_check("Enter the size:", size_options)

    if pizza_size == "large" or pizza_size == "l":
        pizza_size = "large"
        pizza_price = 10
    elif pizza_size == "medium" or pizza_size == "m":
        pizza_size = "medium"
        pizza_price = 7.50
    else:
        pizza_price = 5
        pizza_size = "small"

    extra_toppings = yes_no_check("Would you like extra toppings on your pizza?")
    if extra_toppings == "yes":
        ask_extra_toppings = num_check("Which extra toppings? ", 1, 5)
        print(f"You have purchased {toppings_list[ask_extra_toppings - 1]}!")
        # Add $1 to the pizza price
        pizza_price += extra_topping_price[0]
        # Add extra toppings to customer list
        cust_extra_toppings.append(toppings_list[ask_extra_toppings - 1])
    elif extra_toppings == "no":
        print("No extra toppings will be added to your pizza.")
        cust_extra_toppings.append("None")
    else:
        print("Invalid, Please answer with yes or no.")

        # Calculate total cost for this pizza order
    single_pizza_cost = pizza_price * quantity_made
    total_cost_pizza += single_pizza_cost

    cust_order_dict = {
        'Pizza': cust_pizza,
        'Pizza Amount': quantity_made,
        'Pizza Size': cust_pizza_size,
        'Extra Toppings': cust_extra_toppings,
        'Cost': cust_pizza_cost
    }

    cust_pizza_size.append(pizza_size)
    cust_pizza_cost.append(single_pizza_cost)

    print(f"You have spent a total of ${total_cost_pizza:.2f}")

    # create dataframe / table from dictionary
    cust_order_frame = pandas.DataFrame(cust_order_dict)

    # Rearranging index
    cust_order_frame.index = np.arange(1, len(cust_order_frame) + 1)

    print(cust_order_frame)

    print(f"You currently have {total_pizza_made} pizzas, you can buy {MAX_PIZZAS - total_pizza_made} more pizzas!")

    # ask for another pizza
    print()
    another_pizza = yes_no_check("Would you lke another flavour of pizza? ")

    if another_pizza == "yes":
        continue
    elif another_pizza == "no":
        break
