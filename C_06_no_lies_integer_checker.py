# Functions go here
def int_check(question, low, high):
    """Checks users enter an integer"""

    error = f"Oops - please enter an age between {low} and {high}."

    while True:

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to 'not black' function!

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ", 1, 10)
    print(f"You are {age} years old")
    print(f"{name} bought a ticket")
