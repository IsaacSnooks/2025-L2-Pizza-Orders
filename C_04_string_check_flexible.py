# Functions go here
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
# payment_list = ['cash', 'credit']

while True:
    want_instructions = string_check("Do you want instructions? ")
    print(f"you chose {want_instructions}")
    print()


#   pay_method = string_check("Payment Method: ", payment_list, 2)
#   print(f"You chose {pay_method}")
