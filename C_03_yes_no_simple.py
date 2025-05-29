# functions go here
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question repeats if users don't enter y/n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no\n")


# Main routine goes here

# loop for testing purposes...
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"You choose {want_instructions}\n")