# Functions go here
def int_check(question):
    """Checks users enter an integer between 2 values"""

    error = f"Oops - please enter an integer"

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this cant be blank. Please try again.\n")


def string_check(question, valid_answer=('yes', 'no'), num_letters=1):
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


# Main routine goes here

# initialise variables / non-default options for string checker
payment_list = ['cash', 'credit']

# loop for testing purposes
while True:
    print()

    # ask user for their name (and check it's not blank
    name = not_blank("Name: ")

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask use for payment method(cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_list, 2)
    print(f"{name} has bought a ticket ({pay_method})")
