# Functions go here
def make_statement(statement, decoration):
    """Emphasis headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


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


def instructions():
    make_statement("Instructions", "❕")

    print('''

For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the exit code ('xxx'), the 
program will display the ticket sales information and write the data to a text file.

It will also coose one lucky ticket holder who wins the draw (their ticket is free).

    ''')


make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
print("Program continues...")
