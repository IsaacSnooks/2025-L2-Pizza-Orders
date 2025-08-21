import pandas
import numpy as np
import math

# --- Functions go here ---
def make_statement(statement, decoration):
    """Emphasis headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"


def yes_no_check(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please enter yes / no\n")


def instructions():
    print(make_statement("Instructions", "❕"))
    print('''

For each pizza wanted type...
- The pizza number
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
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_answer}")


def menu():
    print(make_statement("Menu", "📃"))
    print('''
Pizzas: 
1. Peperoni
2. Meat Lovers
3. Hawaiian
4. Cheese
5. Margarita 

Extra Toppings:
1. Cheese
2. Ham
3. Pineapple
4. Bacon
5. Chicken

All Extra Toppings $1
    ''')


def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        print("Sorry, this cant be blank. Please try again.\n")


def num_check(question, low, high):
    """Checks users enter an integer between low and high"""
    while True:
        error = f"Enter a number between {low} and {high}"
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def get_valid_phone():
    while True:
        phone = input("Enter your phone number (NZ only): ").strip()
        if phone.isdigit() and 9 <= len(phone) <= 11 and phone.startswith(("02", "03", "04", "06", "07", "09")):
            return phone
        print("Invalid phone number. Try again (must be NZ format).")


def get_valid_address():
    while True:
        address = input("Enter your address: ").strip()
        if len(address) < 3:
            print("Address is too short, please enter a valid address")
            continue
        if not any(char.isdigit() for char in address):
            print("Address must include a number (e.g. house number).")
            continue
        if not any(char.isalpha() for char in address):
            print("Address must include letters (e.g. street name).")
            continue
        return address


def get_customer_details():
    name = not_blank("Enter your name: ").capitalize()
    phone = get_valid_phone()
    delivery_method = string_check("Pickup or delivery? ", ["pickup", "delivery"], 1)
    address = ""
    if delivery_method == "delivery":
        address = get_valid_address()
    return {
        "name": name,
        "phone": phone,
        "delivery_method": delivery_method,
        "address": address
    }

# --- Main order routine ---
def order():
    global cust_order_frame
    MAX_PIZZAS = 5
    MAX_PER_ORDER = 3

    size_options = ["large", "medium", "small"]

    pizza_list = [
        "Peperoni", "Meat Lovers", "Hawaiian", "Cheese", "Margarita"
    ]
    toppings_list = [
        "Cheese", "Ham", "Pineapple", "Bacon", "Chicken"
    ]

    extra_topping_price = 1

    cust_pizza = []
    cust_pizza_amount = []
    cust_pizza_size = []
    cust_pizza_cost = []
    cust_extra_toppings = []

    total_pizza_made = 0
    total_cost_pizza = 0

    # --- Get customer details once ---
    customer = get_customer_details()

    # --- Add delivery fee if needed ---
    if customer["delivery_method"] == "delivery":
        delivery_fee = 3.00
        print(f"A delivery fee of ${delivery_fee:.2f} has been added to your order.")
        total_cost_pizza += delivery_fee

    # --- Order loop ---
    while True:
        max_remaining = MAX_PIZZAS - total_pizza_made
        if max_remaining == 0:
            print("You have reached the maximum number of pizzas allowed.")
            break
        max_allowed = min(MAX_PER_ORDER, max_remaining)

        pizza_type = num_check("Which pizza? (1-5): ", 1, 5)
        quantity_made = num_check(f"Quantity being made (max {max_allowed}): ", 1, max_allowed)

        total_pizza_made += quantity_made
        cust_pizza.append(pizza_list[pizza_type - 1])
        cust_pizza_amount.append(quantity_made)

        print(f"You have purchased {quantity_made} {pizza_list[pizza_type - 1]} pizzas!")

        print("Sizes and Prices for Pizzas: Large ($10) Medium ($7.50) Small ($5)")
        pizza_size = string_check("Enter the size: ", size_options)
        if pizza_size in ["large", "l"]:
            pizza_size = "large"
            pizza_price = 10
        elif pizza_size in ["medium", "m"]:
            pizza_size = "medium"
            pizza_price = 7.50
        else:
            pizza_size = "small"
            pizza_price = 5
        cust_pizza_size.append(pizza_size)

        extra_toppings = yes_no_check("Would you like extra toppings on your pizza? ")
        if extra_toppings == "yes":
            ask_extra_toppings = num_check("Which extra toppings? (1-5): ", 1, 5)
            topping_name = toppings_list[ask_extra_toppings - 1]
            print(f"You have purchased {topping_name}!")
            pizza_price += extra_topping_price
            cust_extra_toppings.append(topping_name)
        else:
            print("No extra toppings will be added to your pizza.")
            cust_extra_toppings.append("None")

        single_pizza_cost = pizza_price * quantity_made
        total_cost_pizza += single_pizza_cost
        cust_pizza_cost.append(single_pizza_cost)

        cust_order_dict = {
            'Pizza': cust_pizza,
            'Pizza Amount': cust_pizza_amount,
            'Pizza Size': cust_pizza_size,
            'Extra Toppings': cust_extra_toppings,
            'Cost': cust_pizza_cost
        }
        cust_order_frame = pandas.DataFrame(cust_order_dict)
        cust_order_frame.index = np.arange(1, len(cust_order_frame) + 1)

        print(cust_order_frame)
        print(f"Current total: ${total_cost_pizza:.2f}")

        if total_pizza_made >= MAX_PIZZAS:
            print("Max pizzas bought!")
            break

        another_pizza = yes_no_check("Would you like another flavour of pizza? ")
        if another_pizza == "no":
            break

    # --- Final receipt ---
    print(make_statement("FINAL RECEIPT", "🧾"))
    print(f"Customer: {customer['name']}")
    print(f"Phone: {customer['phone']}")
    if customer['delivery_method'] == "delivery":
        print(f"Delivery Address: {customer['address']}")
    else:
        print("Pickup order")
    print()
    print(cust_order_frame)
    print(f"TOTAL COST: ${total_cost_pizza:.2f}")
    print(make_statement("Thank you for shopping at Isaacs Pizzas!", "🍕"))

    confirm = yes_no_check("Do you want to confirm this order? ")
    if confirm == "yes":
        print(make_statement("FINAL RECEIPT", "🧾"))
        print(f"Customer: {customer['name']}")
        print(f"Phone: {customer['phone']}")
        if customer['delivery_method'] == "delivery":
            print(f"Delivery Address: {customer['address']}")
        else:
            print("Pickup order")
        print()
        print(cust_order_frame)
        print(f"TOTAL COST: ${total_cost_pizza:.2f}")
        print(make_statement("Thank you for shopping at Isaacs Pizzas!", "🍕"))
    else:
        print(make_statement("ORDER CANCELLED", "❌"))


# --- Main program ---
print(make_statement("Isaacs Pizza Shop", "🍕"))

if yes_no_check("Do you want to see the instructions? ") == "yes":
    instructions()
if yes_no_check("Do you want to see the menu? ") == "yes":
    menu()

# Start ordering
order()
