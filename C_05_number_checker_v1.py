# Functions go here
def num_check(question, num_type="float", exit_code=None):
    """Checks users enter an integer / float that us nire than zero (or the optional exit code)"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter a number more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main Routine goes here

# loop for testing purposes...
while True:
    print()

    my_float = num_check("Please enter a number more than 0: ", "float")
    print(f"Thanks. You chose {my_float}")
    print()
    my_int = num_check("please enter an integer more than 0:",
                       "integer", "")
    if my_int == "":
        print("You have chosen infinite mode")
    else:
        print(f"Thanks. You chose {my_int}")
